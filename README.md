# Zeon fs (V2) is analog file system AWS S3 with an interesting torrent tracker
- We create an abstract file system that will:
  - store files
  - have access to files according to the CRUD model
  - be able to search for files
  - work with files over the network
  - will be able to synchronize data between selected servers
  - at startup will inform all servers on the network about itself and the list of files
  - make hooks for any file changes
  - client for working with this file system with the ability to download from multiple servers
  - add authorization to servers
  - will have its own internal data transfer protocol


# Installation
- clone this repo :
```
$ git clone https://github.com/KU-Baha/zeon_fs
```
