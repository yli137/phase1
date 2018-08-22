#ifndef __V1LIB__
#define __V1LIB__

void do_memcpy(const int OUTPUTSIZE, const int INPUTSIZE, const int stride, const int NPC);

void inline inlinememcpy(void *dest, const void *src, size_t len);

#endif
