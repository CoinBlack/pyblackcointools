# AGENTS.md - Development Guidelines for Pycryptotools

## Project Overview
Pycryptotools is a Python cryptocurrency library supporting Bitcoin, Bitcoin Cash, Litecoin, Dash, and Dogecoin (mainnet/testnet). It provides wallet management, transaction creation, and blockchain interaction capabilities.

## Build/Test Commands

### Running Tests
```bash
# Run all tests
python -m unittest discover tests -v
python -m pytest tests/ -v

# Run single test method
python -m unittest tests.test_general.TestECCArithmetic.test_all -v
python -m pytest tests/test_general.py::TestECCArithmetic::test_all -v

# Run test class
python -m unittest tests.test_general.TestECCArithmetic -v
python -m pytest tests/test_general.py::TestECCArithmetic -v

# Run test module
python -m unittest tests.test_general -v
python -m pytest tests/test_general.py -v
```

### Package Installation
```bash
# Install in development mode
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

### Building Package
```bash
# Build distribution
python setup.py sdist bdist_wheel

# Upload to PyPI (maintainer only)
python -m twine upload dist/*
```

## Code Style Guidelines

### Import Conventions
- Use wildcard imports for main cryptos modules: `from cryptos import *`
- Use specific imports for types: `from cryptos.types import Tx, TxOut`
- Use relative imports within package: `from .main import *`
- Group imports: standard library, third-party, local imports

### Naming Conventions
- **Classes**: PascalCase (`Bitcoin`, `HDWallet`, `TxInput`)
- **Functions**: snake_case (`privtopub`, `serialize`, `estimate_fee`)
- **Constants**: UPPER_CASE (`P`, `N`, `MAINNET_PRIVATE`)
- **Private methods**: Prefix with underscore (`_get_network_constants`)

### Type Hints
- Always use type hints for function parameters and return values
- Use `TypedDict` for structured data objects
- Use `Optional`, `Union`, `List`, `Dict` from typing module
- Use `NotRequired` from typing_extensions for optional dict fields

### Error Handling
- Use custom exceptions: `NetworkException`, `InvalidPassword`, `TXInvalidError`
- Provide validation functions that return booleans: `is_privkey()`, `is_address()`
- Use graceful degradation - return `None` or `False` on failure
- Chain exceptions in async code to propagate errors properly

### Code Formatting
- Follow PEP 8 with 80-100 character line length
- Use f-strings for string formatting when appropriate
- Add minimal inline comments for complex logic
- Keep functions focused and concise

## Architecture Patterns

### Coin Implementation
- Sync coins inherit from `BaseSyncCoin` in `cryptos/coins/base.py`
- Async coins inherit from `BaseCoin` in `cryptos/coins_async/base.py`
- Each coin must implement: `get_balance`, `get_transactions`, `get_unspent_outputs`, `broadcast_tx`
- Use base test classes from `cryptos/testing/testcases.py` for consistency

### Transaction Handling
- Use `Tx` TypedDict for transaction objects
- Support both legacy and segwit transactions
- Implement proper fee estimation per coin
- Validate transactions before broadcasting

### Wallet Standards
- Support BIP39 mnemonics, BIP32 hierarchical deterministic wallets
- Implement BIP44, BIP49, BIP84 derivation paths
- Support Electrum wallet format compatibility
- Use proper key derivation with PBKDF2

### Network Communication
- Use ElectrumX servers for blockchain data
- Implement both sync and async client interfaces
- Handle SSL connections and server failover
- Implement proper subscription mechanisms

## Testing Guidelines

### Test Structure
- Use `unittest` framework (migrating to pytest)
- Test files mirror source structure in `tests/` directory
- Use static test data (addresses, transactions, expected results)
- Mock network calls for unit tests

### Test Categories
- **Unit tests**: Cryptographic functions, transaction serialization
- **Integration tests**: Network calls, wallet operations
- **Coin tests**: Use base test classes with coin-specific data
- **Async tests**: Use `unittest.IsolatedAsyncioTestCase`

### Test Data
- Use consistent test vectors across all coins
- Include mainnet and testnet examples
- Test edge cases: empty wallets, invalid inputs, network errors
- Verify backward compatibility with existing data

## Security Considerations

### Private Key Handling
- Never log or print private keys
- Use secure random generation for keys
- Implement proper key derivation standards
- Support encrypted key storage

### Transaction Security
- Validate all transaction inputs
- Implement proper fee estimation
- Support multi-signature transactions
- Verify change addresses

### Network Security
- Use SSL/TLS for all network connections
- Validate server certificates
- Implement proper error handling for network failures
- Support proxy connections when needed