FLAGS=-Wall -Isrc/
WASISDK=/opt/wasi-sdk/

all:secureNotes

src/assets.h: ../assets/editPage.html ../assets/loginPage.html ../assets/startPage.html ../assets/viewPage.html ../assets/jquery-3.6.0.min.js  
	python3 process_assets.py

main.o: src/main.c src/www.h
	gcc -c src/main.c ${FLAGS}

www.o: src/www.c src/www.h src/assets.h
	gcc -c src/www.c ${FLAGS}

web_wordpuzzle: main.o www.o
	gcc main.o www.o -o secureNotes ${FLAGS} -O1

secureNotes_debug: src/main.c src/www.h src/www.c src/assets.h
	gcc src/main.c src/www.c ${FLAGS} -DDEBUG -ggdb -o secureNotes_debug

secureNotes.wasm: src/main.c src/www.c src/www.h src/assets.h
	${WASISDK}/bin/clang --sysroot=${WASISDK}/share/wasi-sysroot/ src/main.c src/www.c -Isrc/ ${FLAGS} -O1 -o secureNotes.wasm

secureNotes_debug.wasm: src/main.c src/www.c src/www.h src/assets.h
	${WASISDK}/bin/clang --sysroot=${WASISDK}/share/wasi-sysroot/ src/main.c src/www.c -Isrc/ ${FLAGS} -DDEBUG -o secureNotes.wasm

run_wasm_wasmtime: web_wordpuzzle.wasm
	wasmtime run --tcplisten 127.0.0.1:8080 --env FD_COUNT=1 web_wordpuzzle.wasm

run_wasm_enarx: web_wordpuzzle.wasm
	enarx run --wasmcfgfile ../Enarx.toml web_wordpuzzle.wasm

.phony: clean
clean:
	rm -f *.o secureNotes secureNotes_debug secureNotes.wasm secureNotes_debug.wasm src/assets.h