from datetime import timedelta
from ipaddress import IPv4Address
from pathlib import Path
import os
import yaml


def load_yml(file: Path, encoding="utf-8") -> dict:
    with open(file, "r", encoding=encoding) as f:
        data = yaml.safe_load(f)
    return data


# 获取当前路径
CONFIG_PATH = Path(os.getcwd()) / "configs" / "config.yml"
config = load_yml(CONFIG_PATH)


class BotSelfConfig:
    config: dict = config["BotSelfConfig"]

    host: IPv4Address = IPv4Address(config.get("host", "127.0.0.1"))
    port: int = int(config.get("port", 8080))
    debug: bool = bool(config.get("debug", False))
    superusers: set = set(config.get("superusers", ["21778445"]))
    nickname: set = set(config.get("nickname", ["ATRI", "Atri", "atri", "亚托莉", "アトリ"]))
    command_start: set = set(config.get("command_start", ["", "/"]))
    command_sep: set = set(config.get("command_sep", ["."]))
    session_expire_timeout: timedelta = timedelta(
        seconds=config.get("session_expire_timeout", 60)
    )
    proxy: str = config.get("proxy", None)


class InlineGoCQHTTP:
    config: dict = config["InlineGoCQHTTP"]

    enabled: bool = bool(config.get("enabled", True))
    accounts: list = config.get("accounts", [])
    download_domain: str = config.get("download_domain", "download.fastgit.org")
    download_version: str = str(config.get("download_version", "v1.0.0-rc1"))


class SauceNAO:
    config: dict = config["SauceNAO"]

    key: str = config.get("key", "")


RUNTIME_CONFIG = {
    "host": BotSelfConfig.host,
    "port": BotSelfConfig.port,
    "debug": BotSelfConfig.debug,
    "superusers": BotSelfConfig.superusers,
    "nickname": BotSelfConfig.nickname,
    "command_start": BotSelfConfig.command_start,
    "command_sep": BotSelfConfig.command_sep,
    "session_expire_timeout": BotSelfConfig.session_expire_timeout,
    "gocq_accounts": InlineGoCQHTTP.accounts,
    "gocq_download_domain": InlineGoCQHTTP.download_domain,
    "gocq_version": InlineGoCQHTTP.download_version,
}
