"""Runtime configuration for ltcbech32."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class WalletConfig:
    """Local wallet settings. No remote credentials are stored."""

    network: str = "mainnet"
    rpc_endpoint: str = "http://127.0.0.1:9332"
    storage_dir: str = ".wallets"
    derivation_path: str = "m/84'/2'/0'"
    coin: str = "LTC"
    address_prefix: str = "ltc1q"

    def storage_path(self) -> Path:
        """Return the vault directory, created on first use."""
        path = Path(self.storage_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
