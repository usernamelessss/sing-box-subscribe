# winsw 服务相关
# 定义 winsw 可执行文件和配置文件的路径
$winswExePath = "E:\SingBoxCore\winsw.exe"
$winswConfigPath = "E:\SingBoxCore\winsw.xml"
try {
    # singbox 内核重启：通过 Winsw 服务
    Write-Host "正在关闭 Singbox 服务..."

    # 使用 Start-Process 执行 winsw stop 命令
    # -ArgumentList 参数用来传递命令参数
    Start-Process -FilePath $winswExePath -ArgumentList "stop", $winswConfigPath -NoNewWindow -Wait
    Write-Host "Singbox 服务关闭..."
}
catch {
    Write-Host "Singbox 服务关闭失败: $($_.Exception.Message)" -ForegroundColor Red
}
# 要删除的文件路径数组
$filesToDelete = @(
    "E:\SingBoxCore\cache.db",
    "E:\SingBoxCore\config.json",
    "E:\SingBoxCore\singbox_debug.log"
)

foreach ($file in $filesToDelete) {
    if (Test-Path -Path $file -PathType Leaf) {
        try {
            Write-Host "正在删除文件: '$file'"
            Remove-Item -Path $file -Force
            Write-Host "文件 '$file' 删除成功。"
        }
        catch {
            Write-Error "删除文件 '$file' 时发生错误: $($_.Exception.Message)"
        }
    } else {
        Write-Warning "文件 '$file' 不存在，跳过。"
    }
}

Write-Host "删除操作完成。"

# 定义路径变量
$scriptPath = "E:\SingBoxCore\sub_convert_home\sing-box-subscribe\main.py"
$destinationPath = "E:\SingBoxCore\config.json"
$tempConfigPath = (Split-Path -Path $scriptPath) + "\config.json"



try {
    # 切换到脚本所在目录
    Set-Location (Split-Path -Path $scriptPath)
    
    Write-Host "正在执行 Python 脚本..."
    
    # 执行Python脚本，并捕获输出
    $process = Start-Process -FilePath "python.exe" -ArgumentList $scriptPath -NoNewWindow -Wait -PassThru
    
    if ($process.ExitCode -ne 0) {
        throw "Python 脚本执行失败，退出代码: $($process.ExitCode)"
    }
    
    # 检查生成的文件是否存在
    if (-not (Test-Path -Path $tempConfigPath)) {
        throw "Python 脚本未生成 config.json 文件。"
    }
    
    # 复制并替换文件
    Write-Host "正在复制并替换文件..."
    Copy-Item -Path $tempConfigPath -Destination $destinationPath -Force
    Write-Host "文件替换成功！"
    
    # singbox 内核重启：通过 Winsw 服务
    Write-Host "正在重启 Singbox 服务..."

    # 使用 Start-Process 执行 winsw start 命令
    # -ArgumentList 参数用来传递命令参数
    Start-Process -FilePath $winswExePath -ArgumentList "start", $winswConfigPath -NoNewWindow -Wait
    Write-Host "Singbox 服务重启成功。"
}
catch {
    Write-Host "操作失败: $($_.Exception.Message)" -ForegroundColor Red
}