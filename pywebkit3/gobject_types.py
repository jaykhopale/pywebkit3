from ctypes import cdll, CDLL, c_int, CFUNCTYPE, c_void_p, Structure

cdll.LoadLibrary("libgobject-2.0.so")
libgobject = CDLL("libgobject-2.0.so")

GType = c_int
G_TYPE_INVALID                  = c_int (0)
G_TYPE_NONE                     = c_int (1)
G_TYPE_INTERFACE                = c_int (2)
G_TYPE_CHAR                     = c_int (3)
G_TYPE_UCHAR                    = c_int (4)
G_TYPE_BOOLEAN                  = c_int (5)
G_TYPE_INT                      = c_int (24)
G_TYPE_UINT                     = c_int (7)
G_TYPE_LONG                     = c_int (8)
G_TYPE_ULONG                    = c_int (9)
G_TYPE_INT64                    = c_int (10)
G_TYPE_UINT64                   = c_int (11)
G_TYPE_ENUM                     = c_int (12)
G_TYPE_FLAGS                    = c_int (13)
G_TYPE_FLOAT                    = c_int (14)
G_TYPE_DOUBLE                   = c_int (15)
G_TYPE_STRING                   = c_int (16)
G_TYPE_POINTER                  = c_int (17)
G_TYPE_BOXED                    = c_int (18)
G_TYPE_PARAM                    = c_int (19)
G_TYPE_OBJECT                   = c_int (20)
G_TYPE_VARIANT                  = c_int (21)


GSourceFunc = CFUNCTYPE(c_int, c_void_p)
GDestroyNotifyCB = CFUNCTYPE(None, c_void_p)
GDuplicateFunc = CFUNCTYPE( c_void_p, c_void_p, c_void_p)
GPollFunc = CFUNCTYPE(c_int, c_void_p, c_uint, c_int)
GObjectGetPropertyFunc = CFUNCTYPE( None,  c_void_p, c_uint, c_void_p, c_void_p)
GObjectSetPropertyFunc = CFUNCTYPE( None,  c_void_p, c_uint, c_void_p, c_void_p)
GWeakNotify = CFUNCTYPE(None, c_void_p, c_void_p)
GTogleNotify = CFUNCTYPE( None, c_void_p, c_void_p, c_int)
GValueTransform = CFUNCTYPE( None, c_void_p, c_void_p)
GCompareFunc = CFUNCTYPE( c_int, c_void_p, c_void_p)
GCompareDataFunc = CFUNCTYPE( c_int, c_void_p, c_void_p)

def gvalue_from_int( val):
    from _gtk3_GValue import GValue
    gval = GValue()
    gavl.init(G_TYPE_INT)
    gval.set_int( val)
    return gval
    
