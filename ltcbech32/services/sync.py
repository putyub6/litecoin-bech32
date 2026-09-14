"""Pull stub balances into the active vault."""

from __future__ import annotations

from ltcbech32.chain.rpc import RpcClient
from ltcbech32.config import WalletConfig
from ltcbech32.models import Vault


class SyncEngine:
    """Refresh account balances through :class:`RpcClient`."""

    def __init__(self, config: WalletConfig | None = None) -> None:
        self.client = RpcClient(config or WalletConfig())

    def sync(self, vault: Vault) -> Vault:
        """Mutate ``vault`` balances in place and return it."""
        for account in vault.accounts:
            account.balance = self.client.get_balance(account.address)
        return vault
