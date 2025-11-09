[Browse Collections](https://docs.trychroma.com/docs/cli/browse)
[Copy Collections](https://docs.trychroma.com/docs/cli/copy)
[DB Management](https://docs.trychroma.com/docs/cli/db)
[Install Sample Apps](https://docs.trychroma.com/docs/cli/sample-apps)
[Login](https://docs.trychroma.com/docs/cli/login)
[Profile Management](https://docs.trychroma.com/docs/cli/profile)
[Run a Chroma Server](https://docs.trychroma.com/docs/cli/run)
[Update the CLI](https://docs.trychroma.com/docs/cli/update)
[Vacuum](https://docs.trychroma.com/docs/cli/vacuum)
w-5 h-5
# Persistent Client
PythonTypescript
You can configure Chroma to save and load the database from your local machine, using the PersistentClient.
Data will be persisted automatically and loaded on start (if it exists).
Python
```

import chromadb
client = chromadb.PersistentClient(path="/path/to/save/to")


```

The path is where Chroma will store its database files on disk, and load them on start. If you don't provide a path, the default is .chroma
The client object has a few useful convenience methods.
  * heartbeat() - returns a nanosecond heartbeat. Useful for making sure the client remains connected.
  * reset() - empties and completely resets the database. ⚠️ This is destructive and not reversible.


PythonTypescript
```

client.heartbeat()
client.reset()


```

[Ephemeral Client](https://docs.trychroma.com/docs/run-chroma/ephemeral-client)[Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)
[Edit this page on GitHub](https://github.com/chroma-core/chroma/tree/main/docs/docs.trychroma.com/markdoc/content/docs/run-chroma/persistent-client.md)
Ask this Page
Ask this Page
On this page
[Persistent Client](https://docs.trychroma.com/docs/run-chroma/persistent-client#persistent-client)
NEW
Chroma Cloud