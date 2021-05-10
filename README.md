# dork-search

### Installation

1. Get an API Key at [https://serpapi.com/](https://serpapi.com/)
2. Clone the repo
   ```sh
   $ git clone https://github.com/f4tih35/dork-search.git
   ```
3. Install requirements
   ```sh
   $ pip install requirements
   ```
4. Enter your API in `config.py`
   ```PY
   API_KEY = 'ENTER YOUR API'

### Usage
```sh
$ python app.py -k [keyword] -s [suffix] -t [type]
```

### Example
```sh
$ python app.py -k scrum -s -t ZOOM_MEETINGS
```
```sh
$ python app.py -k -s -t GOV_RESTRICTED_DOC
```
```bash
$ python app.py -k school -s .com.br -t OPEN_FTP_SERVER
```
You can find all types in ```search_type_enum.py``` file
