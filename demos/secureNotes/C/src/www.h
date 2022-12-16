#ifndef www_h__
#define www_h__

#include <stdint.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <llist.h> 

// Modelled after
// https://github.com/Dungyichao/http_server/blob/master/src/helloworld.cpp

// typedef unsigned char byte;
// typedef void (*web_handler)(*byte, *uint32_t, **byte, *uint32_t, byte[10]); // request, request size, response, response size, type

#define WORD_SIZE 5

typedef struct {
    node_t notes;
    node_t unique_identifiers; 
    int server_fd;
    struct sockaddr_in address;
} WebServer;

#ifdef __wasi__
WebServer* CreateWebServerWithFD(int sd);
#else
WebServer* CreateWebServerWithPort(uint16_t port);
#endif

void DestroyWebServer(WebServer* server);
void RunWebServer(WebServer *server);

ssize_t write_all(const int fd, const void *buf, const size_t n);

#endif