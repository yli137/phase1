#ifndef __V1LIB__
#define __V1LIB__

#define _MM_HINT_T0 HINT0
#define _MM_HINT_T1 HINT1
#define _MM_HINT_T2 HINT2
#define _MM_HINT_NTA HINTNTA

void do_memcpy(const int OUTPUTSIZE, const int INPUTSIZE, const int stride, const int NPC);

void inline inlinememcpy(void *dest, const void *src, size_t len);

#endif
