"""gate CI 在干净 checkout 上跑通用 pytest 所需的引导。

1) app/config.py 在 import 期就实例化 Config() 读 config.yaml —— CI 没有本地配置,
   用仓库自带的示例配置生成一份(本地已有 config.yaml 时不动)。
2) 两个连真实服务的手动验证脚本(Obsidian REST / 企微真发通知)不属于 CI 单测,
   collect 阶段排除,避免在 CI 里打真实服务。
"""
import shutil
from pathlib import Path

_root = Path(__file__).parent
if not (_root / "config.yaml").exists():
    shutil.copyfile(_root / "config..example.yaml", _root / "config.yaml")

collect_ignore = [
    "tests/test_obsidian_connection.py",   # 连真实 Obsidian REST API
    "tests/test_wecom_notification.py",    # 真发企业微信通知
    "tests/test_markdown_converter.py",    # 依赖本地 debug/ 产物(不入库),非封闭单测
]
