# sheets-backup

Back up a Google Sheet to a git repository.

## Usage

Set the following environment variables:

- `GIT_REMOTE` - Remote of the git repository to push to. This must use the SSH
  protocol. Note: this repo will be pulled from on first start.
- `GIT_SSH_AUTH_KEY` - SSH key to authenticate to the remote repo when pushing
  with.

## License

See [LICENSE](LICENSE).
