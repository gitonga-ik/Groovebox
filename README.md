# Groovebox

## Music Sharing & Discovery Platform

Groovebox is a simple music application that allows **artists** to upload and manage songs and playlists, **listeners** to discover and enjoy music, and **developers** to access music data through a REST API.

---

## Key Features

### Artists

- Register as an artist
- Upload, edit, and delete songs
- Create and manage playlists
- Public artist profile

### Listeners

- Register as a listener
- Browse songs and playlists
- View artist profiles
- Create personal playlists

### Developers

- REST API for songs, playlists, and authentication
- Token-based authentication
- Public and protected endpoints

---

## Application Interfaces

Groovebox provides two main ways to interact with the system:

1. **Web Interface (HTML pages)**  
2. **REST API (JSON)**  

---

## Web Application Endpoints

### Music Pages (`/v1/`)

- `GET /v1/` or `/v1/home/` — Home page (recent songs & playlists)
- `GET /v1/songs/<id>` — View song details
- `GET, POST /v1/songs/create` — Upload a song (artist only)
- `GET, POST /v1/songs/update/<id>` — Edit a song (artist only)
- `POST /v1/songs/delete/<id>` — Delete a song (artist only)
- `GET /v1/artists/<id>` — View artist profile and songs

#### Playlists

- `GET /v1/playlist/<id>` — View playlist
- `GET, POST /v1/playlist/create` — Create playlist
- `GET, POST /v1/playlist/update/<id>` — Update playlist
- `POST /v1/playlist/delete/<id>` — Delete playlist

---

### Account Pages (`/accounts/`)

- `GET, POST /accounts/register/` — Register as listener
- `GET, POST /accounts/register/artist` — Register as artist
- `GET, POST /accounts/login/` — Log in
- `GET /accounts/logout/` — Log out
- `GET, POST /accounts/profile/<id>` — View or update profile

---

## REST API Endpoints (`/v2/`)

### Authentication

- `POST /v2/listener-register/` — Register listener
- `POST /v2/artist-register/` — Register artist
- `POST /v2/login/` — Log in and receive token
- `POST /v2/get-token/` — Get current user token

---

### Songs API

- `GET /v2/songs/` — List songs (search & filter supported)
- `POST /v2/songs/` — Upload song (artist only)
- `GET /v2/songs/{id}/` — Retrieve song
- `PUT/PATCH /v2/songs/{id}/` — Update song (artist only)
- `DELETE /v2/songs/{id}/` — Delete song (artist only)

---

### Playlists API

- `GET /v2/playlists/` — List playlists
- `POST /v2/playlists/` — Create playlist (authenticated)
- `GET /v2/playlists/{id}/` — Retrieve playlist
- `PUT/PATCH /v2/playlists/{id}/` — Update playlist (owner only)
- `DELETE /v2/playlists/{id}/` — Delete playlist (owner only)

---

## Authentication Requirements

- Public access for browsing content
- Login required for creating or managing songs and playlists
- API uses token authentication  
