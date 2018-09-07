#ifndef __INLINEMEM__
#define __INLINEMEM__
#include<string.h>
inline void _memcpy(void *dest, const void *src, size_t n){
	memcpy(dest, src, n);
}

#endif
