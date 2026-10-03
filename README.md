# IRIS public automatic repair demo

A disposable, author-created Python HTTP service for observing LikeLion automatic code repair.
The initial commit deliberately omits the colon in the `add` function definition, causing the Docker build to fail.
The expected repair restores the colon while preserving the compilation check.

After repair, `/health` returns `{"status":"ok"}` and `/add?a=2&b=5` returns `{"result":7}`.
No credentials, external databases, packages, or manual environment settings are required.
