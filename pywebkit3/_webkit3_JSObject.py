# Copyright, John Rusnak, 2012
    # This code binding is available under the license agreement of the LGPL with
    # an additional constraint described below,
    # and with the understanding that the webkit API is copyright protected
    # by Apple Computer, Inc. (see below).
    # There is an  additional constraint that any derivatives of this work aimed
    # at providing bindings to GObject, GTK, GDK, or WebKit be strictly
    # python-only bindings with no native code.
    # * THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    #
    # ******************************************************
    # For the API:
    # /*
    # * Copyright (C) 2006 Apple Computer, Inc.  All rights reserved.
    # *
    # * Redistribution and use in source and binary forms, with or without
    # * modification, are permitted provided that the following conditions
    # * are met:
    # * 1. Redistributions of source code must retain the above copyright
    # *    notice, this list of conditions and the following disclaimer.
    # * 2. Redistributions in binary form must reproduce the above copyright
    # *    notice, this list of conditions and the following disclaimer in the
    # *    documentation and/or other materials provided with the distribution.
    # *
    # * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
    # * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    # * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
    # * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
    # * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
    # * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
    # * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    # * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
    # * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    # */
from ctypes import *
from gtk3_types import *
from webkit3_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitNetworkResponse = POINTER(c_int)
_GdkPixbuf = POINTER(c_int)
__GtkRequisition = POINTER(c_int)
_GtkRcStyle = POINTER(c_int)
__GtkRegionFlags = POINTER(c_int)
_GtkBin = POINTER(c_int)
_GtkWindow = POINTER(c_int)
__cairo_font_options_t = POINTER(c_int)
__JSValue = POINTER(c_int)
_JSContext = POINTER(c_int)
_GtkIconFactory = POINTER(c_int)
__GdkAtom = POINTER(c_int)
__GdkTimeCoord = POINTER(c_int)
__GtkWidgetPath = POINTER(c_int)
__GClosure = POINTER(c_int)
_GdkDisplay = POINTER(c_int)
__GtkStyleProvider = POINTER(c_int)
__WebKitWebWindowFeatures = POINTER(c_int)
_JSObject = POINTER(c_int)
_GBytes = POINTER(c_int)
_GScanner = POINTER(c_int)
_PangoFont = POINTER(c_int)
_GtkStyleContext = POINTER(c_int)
__GtkTextBuffer = POINTER(c_int)
_GtkTargetList = POINTER(c_int)
__WebKitWebSettings = POINTER(c_int)
_GdkAppLaunchContext = POINTER(c_int)
_GtkContainer = POINTER(c_int)
__PangoLayout = POINTER(c_int)
_WebKitWebBackForwardList = POINTER(c_int)
__GParamSpec = POINTER(c_int)
__PangoAttrIterator = POINTER(c_int)
_GtkIconSet = POINTER(c_int)
_GtkSelectionData = POINTER(c_int)
_GtkWindowGroup = POINTER(c_int)
_GtkAdjustment = POINTER(c_int)
_JSGlobalContext = POINTER(c_int)
_GApplication = POINTER(c_int)
_PangoLogAttr = POINTER(c_int)
__PangoContext = POINTER(c_int)
__JSPropertyNameArray = POINTER(c_int)
_WebKitWebSettings = POINTER(c_int)
__GtkPathPriorityType = POINTER(c_int)
__JSClass = POINTER(c_int)
__WebKitWebHistoryItem = POINTER(c_int)
_JSValue = POINTER(c_int)
__GtkSettings = POINTER(c_int)
__PangoFontMap = POINTER(c_int)
__JSString = POINTER(c_int)
__PangoAttrList = POINTER(c_int)
_PangoMatrix = POINTER(c_int)
_GtkApplication = POINTER(c_int)
__GObject = POINTER(c_int)
__GtkContainerClass = POINTER(c_int)
__PangoAnalysis = POINTER(c_int)
_PangoFontDescription = POINTER(c_int)
__GdkCursor = POINTER(c_int)
_WebKitWebInspector = POINTER(c_int)
__GScanner = POINTER(c_int)
__GtkWidgetClass = POINTER(c_int)
__GObjectClass = POINTER(c_int)
__GtkAdjustment = POINTER(c_int)
_GdkDragContext = POINTER(c_int)
__GdkDisplay = POINTER(c_int)
_GtkSettings = POINTER(c_int)
_GdkScreen = POINTER(c_int)
_PangoFontMetrics = POINTER(c_int)
_GdkVisual = POINTER(c_int)
_PangoFontMap = POINTER(c_int)
_GSList = POINTER(c_int)
_WebKitWebFrame = POINTER(c_int)
_JSString = POINTER(c_int)
__GActionGroup = POINTER(c_int)
_GtkWidget = POINTER(c_int)
__WebKitNetworkRequest = POINTER(c_int)
__GdkWindow = POINTER(c_int)
__PangoFontFamily = POINTER(c_int)
__JSContextGroup = POINTER(c_int)
__cairo_region_t = POINTER(c_int)
_PangoFontset = POINTER(c_int)
_GdkWindow = POINTER(c_int)
__PangoFontDescription = POINTER(c_int)
__GtkBorder = POINTER(c_int)
__GError = POINTER(c_int)
__PangoCoverage = POINTER(c_int)
_WebKitViewportAttributes = POINTER(c_int)
_JSClass = POINTER(c_int)
_WebKitWebHistoryItem = POINTER(c_int)
__cairo_t = POINTER(c_int)
__GWeakRef = POINTER(c_int)
__GdkVisual = POINTER(c_int)
__GdkEventButton = POINTER(c_int)
__GCancellable = POINTER(c_int)
__GIcon = POINTER(c_int)
_GList = POINTER(c_int)
__GtkAccelGroup = POINTER(c_int)
_GObject = POINTER(c_int)
__GtkIconSource = POINTER(c_int)
__GFile = POINTER(c_int)
__JSContext = POINTER(c_int)
__GtkAllocation = POINTER(c_int)
__GtkWidget = POINTER(c_int)
_PangoLayoutLine = POINTER(c_int)
__GtkIconSet = POINTER(c_int)
_WebKitWebView = POINTER(c_int)
__PangoTabArray = POINTER(c_int)
_WebKitHitTestResult = POINTER(c_int)
__GValue = POINTER(c_int)
_GdkDeviceManager = POINTER(c_int)
_GdkCursor = POINTER(c_int)
_WebKitDOMDocument = POINTER(c_int)
__PangoMatrix = POINTER(c_int)
__GtkPrintOperation = POINTER(c_int)
_PangoContext = POINTER(c_int)
__GList = POINTER(c_int)
__WebKitWebView = POINTER(c_int)
_WebKitWebWindowFeatures = POINTER(c_int)
_PangoCoverage = POINTER(c_int)
_GParamSpec = POINTER(c_int)
__PangoRectangle = POINTER(c_int)
__GdkRGBA = POINTER(c_int)
__JSPropertyNameAccumulator = POINTER(c_int)
__PangoGlyphString = POINTER(c_int)
__JSGlobalContext = POINTER(c_int)
_WebKitSecurityOrigin = POINTER(c_int)
__GdkEventKey = POINTER(c_int)
__GSList = POINTER(c_int)
__GdkWindowAttr = POINTER(c_int)
_SoupMessage = POINTER(c_int)
_WebKitWebDataSource = POINTER(c_int)
_GdkAtom = POINTER(c_int)
__GdkColor = POINTER(c_int)
_JSContextGroup = POINTER(c_int)
__GdkRectangle = POINTER(c_int)
__PangoLanguage = POINTER(c_int)
_PangoAttrList = POINTER(c_int)
__gunichar = POINTER(c_int)
__GdkWMDecoration = POINTER(c_int)
__PangoLogAttr = POINTER(c_int)
_PangoLayout = POINTER(c_int)
_JSPropertyNameArray = POINTER(c_int)
__JSObject = POINTER(c_int)
__WebKitDOMNode = POINTER(c_int)
_GtkStyle = POINTER(c_int)
__GParameter = POINTER(c_int)
__GtkStyle = POINTER(c_int)
_GdkDevice = POINTER(c_int)
__GtkWindow = POINTER(c_int)
__cairo_pattern_t = POINTER(c_int)
__GdkPixbuf = POINTER(c_int)
_GtkWidgetPath = POINTER(c_int)
__GtkTargetEntry = POINTER(c_int)
__GtkApplication = POINTER(c_int)
_GtkClipboard = POINTER(c_int)
_PangoTabArray = POINTER(c_int)
__GdkScreen = POINTER(c_int)
_PangoLanguage = POINTER(c_int)
__GdkDevice = POINTER(c_int)
_GByteArray = POINTER(c_int)
"""Enumerations"""
GdkVisualType = c_int
GdkByteOrder = c_int
GtkIconSize = c_int
GdkPixbufError = c_int
GdkColorspace = c_int
GdkPixbufAlphaMode = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
GdkWindowType = c_int
GdkWindowWindowClass = c_int
GdkWindowHints = c_int
GdkGravity = c_int
GdkWindowEdgeh = c_int
GdkWindowTypeHint = c_int
GdkWindowAttributesType = c_int
GdkFilterReturn = c_int
GdkModifierType = c_int
GdkWMDecoration = c_int
GdkWMFunction = c_int
GdkInputSource = c_int
GdkInputMode = c_int
GdkAxisUse = c_int
GdkDeviceType = c_int
GdkGrabOwnership = c_int
GdkCursorType = c_int
PangoStyle = c_int
PangoWeight = c_int
PangoVariant = c_int
PangoStretch = c_int
PangoFontMask = c_int
GtkRcFlags = c_int
GtkRcTokenType = c_int
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GApplicationFlags = c_int
WebKitNavigationResponse = c_int
WebKitWebViewTargetInfo = c_int
WebKitWebViewViewMode = c_int
WebKitLoadStatus = c_int
WebKitEditingBehavior = c_int

class JSObject( object):
    """Class JSObject Constructors"""
    def __init__(self, obj = None):
        self._object = obj
    """Methods"""
    def GetProperty(  self, ctx, propertyName, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectGetProperty.restype = _JSValue
        libwebkit3.JSObjectGetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=libwebkit3.JSObjectGetProperty( ctx,self._object,propertyName,exception )  or POINTER(c_int)())

    def JSPropertyNameAccumulatorAddName(  self, accumulator, propertyName, ):
        if accumulator: accumulator = accumulator._object
        else: accumulator = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()

        libwebkit3.JSPropertyNameAccumulatorAddName.argtypes = [_JSObject,_JSPropertyNameAccumulator,_JSString]
        
        libwebkit3.JSPropertyNameAccumulatorAddName( self._object,accumulator,propertyName )

    def SetPrototype(  self, ctx, value, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()

        libwebkit3.JSObjectSetPrototype.argtypes = [_JSContext,_JSObject,_JSValue]
        
        libwebkit3.JSObjectSetPrototype( ctx,self._object,value )

    def HasProperty(  self, ctx, propertyName, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()

        libwebkit3.JSObjectHasProperty.restype = bool
        libwebkit3.JSObjectHasProperty.argtypes = [_JSContext,_JSObject,_JSString]
        
        return libwebkit3.JSObjectHasProperty( ctx,self._object,propertyName )

    def GetPrototype(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSObjectGetPrototype.restype = _JSValue
        libwebkit3.JSObjectGetPrototype.argtypes = [_JSContext,_JSObject]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=libwebkit3.JSObjectGetPrototype( ctx,self._object )  or POINTER(c_int)())

    def CallAsConstructor(  self, ctx, argumentCount, arguments, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectCallAsConstructor.restype = _JSObject
        libwebkit3.JSObjectCallAsConstructor.argtypes = [_JSContext,_JSObject,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject(None,None,None,None, obj=libwebkit3.JSObjectCallAsConstructor( ctx,self._object,argumentCount,arguments,exception )  or POINTER(c_int)())

    def JSPropertyNameArrayRelease(  self, array, ):
        if array: array = array._object
        else: array = POINTER(c_int)()

        libwebkit3.JSPropertyNameArrayRelease.argtypes = [_JSObject,_JSPropertyNameArray]
        
        libwebkit3.JSPropertyNameArrayRelease( self._object,array )

    def DeleteProperty(  self, ctx, propertyName, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectDeleteProperty.restype = bool
        libwebkit3.JSObjectDeleteProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue]
        
        return libwebkit3.JSObjectDeleteProperty( ctx,self._object,propertyName,exception )

    def IsConstructor(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSObjectIsConstructor.restype = bool
        libwebkit3.JSObjectIsConstructor.argtypes = [_JSContext,_JSObject]
        
        return libwebkit3.JSObjectIsConstructor( ctx,self._object )

    def SetPropertyAtIndex(  self, ctx, propertyIndex, value, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyIndex: propertyIndex = propertyIndex._object
        else: propertyIndex = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectSetPropertyAtIndex.argtypes = [_JSContext,_JSObject,unsigned,_JSValue,_JSValue]
        
        libwebkit3.JSObjectSetPropertyAtIndex( ctx,self._object,propertyIndex,value,exception )

    def SetPrivate(  self, data, ):

        libwebkit3.JSObjectSetPrivate.restype = bool
        libwebkit3.JSObjectSetPrivate.argtypes = [_JSObject,c_char_p]
        
        return libwebkit3.JSObjectSetPrivate( self._object,data )

    def JSClassRelease(  self, jsClass, ):
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()

        libwebkit3.JSClassRelease.argtypes = [_JSObject,_JSClass]
        
        libwebkit3.JSClassRelease( self._object,jsClass )

    def CallAsFunction(  self, ctx, thisObject, argumentCount, arguments, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if thisObject: thisObject = thisObject._object
        else: thisObject = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectCallAsFunction.restype = _JSValue
        libwebkit3.JSObjectCallAsFunction.argtypes = [_JSContext,_JSObject,_JSObject,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=libwebkit3.JSObjectCallAsFunction( ctx,self._object,thisObject,argumentCount,arguments,exception )  or POINTER(c_int)())

    def CopyPropertyNames(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSObjectCopyPropertyNames.restype = _JSPropertyNameArray
        libwebkit3.JSObjectCopyPropertyNames.argtypes = [_JSContext,_JSObject]
        from pywebkit3.javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=libwebkit3.JSObjectCopyPropertyNames( ctx,self._object )  or POINTER(c_int)())

    def GetPropertyAtIndex(  self, ctx, propertyIndex, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyIndex: propertyIndex = propertyIndex._object
        else: propertyIndex = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectGetPropertyAtIndex.restype = _JSValue
        libwebkit3.JSObjectGetPropertyAtIndex.argtypes = [_JSContext,_JSObject,unsigned,_JSValue]
        from pywebkit3.javascriptcore import JSValue
        return JSValue( obj=libwebkit3.JSObjectGetPropertyAtIndex( ctx,self._object,propertyIndex,exception )  or POINTER(c_int)())

    def GetPrivate(  self, ):

        libwebkit3.JSObjectGetPrivate.restype = c_char_p
        libwebkit3.JSObjectGetPrivate.argtypes = [_JSObject]
        
        return libwebkit3.JSObjectGetPrivate( self._object )

    def SetProperty(  self, ctx, propertyName, value, attributes, exception, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if propertyName: propertyName = propertyName._object
        else: propertyName = POINTER(c_int)()
        if value: value = value._object
        else: value = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()

        libwebkit3.JSObjectSetProperty.argtypes = [_JSContext,_JSObject,_JSString,_JSValue,JSPropertyAttributes,_JSValue]
        
        libwebkit3.JSObjectSetProperty( ctx,self._object,propertyName,value,attributes,exception )

    def IsFunction(  self, ctx, ):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()

        libwebkit3.JSObjectIsFunction.restype = bool
        libwebkit3.JSObjectIsFunction.argtypes = [_JSContext,_JSObject]
        
        return libwebkit3.JSObjectIsFunction( ctx,self._object )

    @staticmethod
    def JSClassRetain( jsClass,):
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        libwebkit3.JSClassRetain.restype = _JSClass
        libwebkit3.JSClassRetain.argtypes = [_JSClass]
        from pywebkit3.javascriptcore import JSClass
        return JSClass( obj=    libwebkit3.JSClassRetain(jsClass, )
  or POINTER(c_int)())
    @staticmethod
    def MakeError( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libwebkit3.JSObjectMakeError.restype = _JSObject
        libwebkit3.JSObjectMakeError.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeError(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFunctionWithCallback( ctx, name, callAsFunction,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if name: name = name._object
        else: name = POINTER(c_int)()
        libwebkit3.JSObjectMakeFunctionWithCallback.restype = _JSObject
        libwebkit3.JSObjectMakeFunctionWithCallback.argtypes = [_JSContext,_JSString,JSObjectCallAsFunctionCallback]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeFunctionWithCallback(ctx, name, callAsFunction, )
  or POINTER(c_int)())
    @staticmethod
    def MakeArray( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libwebkit3.JSObjectMakeArray.restype = _JSObject
        libwebkit3.JSObjectMakeArray.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeArray(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def MakeConstructor( ctx, jsClass, callAsConstructor,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        libwebkit3.JSObjectMakeConstructor.restype = _JSObject
        libwebkit3.JSObjectMakeConstructor.argtypes = [_JSContext,_JSClass,JSObjectCallAsConstructorCallback]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeConstructor(ctx, jsClass, callAsConstructor, )
  or POINTER(c_int)())
    @staticmethod
    def MakeDate( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libwebkit3.JSObjectMakeDate.restype = _JSObject
        libwebkit3.JSObjectMakeDate.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeDate(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def JSPropertyNameArrayRetain( array,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        libwebkit3.JSPropertyNameArrayRetain.restype = _JSPropertyNameArray
        libwebkit3.JSPropertyNameArrayRetain.argtypes = [_JSPropertyNameArray]
        from pywebkit3.javascriptcore import JSPropertyNameArray
        return JSPropertyNameArray( obj=    libwebkit3.JSPropertyNameArrayRetain(array, )
  or POINTER(c_int)())
    @staticmethod
    def JSPropertyNameArrayGetNameAtIndex( array, index,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        libwebkit3.JSPropertyNameArrayGetNameAtIndex.restype = _JSString
        libwebkit3.JSPropertyNameArrayGetNameAtIndex.argtypes = [_JSPropertyNameArray,size_t]
        from pywebkit3.javascriptcore import JSString
        return JSString( obj=    libwebkit3.JSPropertyNameArrayGetNameAtIndex(array, index, )
  or POINTER(c_int)())
    @staticmethod
    def MakeFunction( ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if name: name = name._object
        else: name = POINTER(c_int)()
        if parameterCount: parameterCount = parameterCount._object
        else: parameterCount = POINTER(c_int)()
        if parameterNames: parameterNames = parameterNames._object
        else: parameterNames = POINTER(c_int)()
        if body: body = body._object
        else: body = POINTER(c_int)()
        if sourceURL: sourceURL = sourceURL._object
        else: sourceURL = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libwebkit3.JSObjectMakeFunction.restype = _JSObject
        libwebkit3.JSObjectMakeFunction.argtypes = [_JSContext,_JSString,unsigned,_JSString,_JSString,_JSString,int,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeFunction(ctx, name, parameterCount, parameterNames, body, sourceURL, startingLineNumber, exception, )
  or POINTER(c_int)())
    @staticmethod
    def Make( ctx, jsClass, data,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if jsClass: jsClass = jsClass._object
        else: jsClass = POINTER(c_int)()
        libwebkit3.JSObjectMake.restype = _JSObject
        libwebkit3.JSObjectMake.argtypes = [_JSContext,_JSClass,c_char_p]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMake(ctx, jsClass, data, )
  or POINTER(c_int)())
    @staticmethod
    def JSPropertyNameArrayGetCount( array,):
        if array: array = array._object
        else: array = POINTER(c_int)()
        libwebkit3.JSPropertyNameArrayGetCount.restype = size_t
        libwebkit3.JSPropertyNameArrayGetCount.argtypes = [_JSPropertyNameArray]
        
        return     libwebkit3.JSPropertyNameArrayGetCount(array, )

    @staticmethod
    def MakeRegExp( ctx, argumentCount, arguments, exception,):
        if ctx: ctx = ctx._object
        else: ctx = POINTER(c_int)()
        if arguments: arguments = arguments._object
        else: arguments = POINTER(c_int)()
        if exception: exception = exception._object
        else: exception = POINTER(c_int)()
        libwebkit3.JSObjectMakeRegExp.restype = _JSObject
        libwebkit3.JSObjectMakeRegExp.argtypes = [_JSContext,size_t,_JSValue,_JSValue]
        from pywebkit3.javascriptcore import JSObject
        return JSObject( obj=    libwebkit3.JSObjectMakeRegExp(ctx, argumentCount, arguments, exception, )
  or POINTER(c_int)())
    @staticmethod
    def JSClassCreate( definition,):
        libwebkit3.JSClassCreate.restype = _JSClass
        libwebkit3.JSClassCreate.argtypes = [POINTER(JSClassDefinition)]
        from pywebkit3.javascriptcore import JSClass
        return JSClass( obj=    libwebkit3.JSClassCreate(definition, )
  or POINTER(c_int)())
