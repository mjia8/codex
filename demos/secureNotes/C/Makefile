FLAGS=-Wall -Isrc/
WASISDK=/opt/wasi-sdk/

all:secureNotes

src/assets.h: ../assets/notes.html 
	python3 process_assets.py