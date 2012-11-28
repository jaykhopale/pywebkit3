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
from gtk3_types import *
    
    
"""Derived Pointer Types"""
__GtkRcStyle = POINTER(c_int)
__GdkGeometry = POINTER(c_int)
_WebKitWebPolicyDecision = POINTER(c_int)
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
_GtkScrolledWindow = POINTER(c_int)
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
_GtkOffscreenWindow = POINTER(c_int)
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
_PangoAnalysis = POINTER(c_int)
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
_WebKitGeolocationPolicyDecision = POINTER(c_int)
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
PangoWrapMode = c_int
PangoEllipsizeMode = c_int
PangoAlignment = c_int
GtkWidgetHelpType = c_int
GtkTextDirection = c_int
GtkSizeRequestMode = c_int
GtkAlign = c_int
WebKitLoadStatus = c_int

import _gtk3_GtkBin
class GtkScrolledWindow( _gtk3_GtkBin.GtkBin):
    """Class GtkScrolledWindow Constructors"""
    def __init__( self, hadjustment, vadjustment,  obj = None):
        if obj: self._object = obj
        else:
            libgtk3.gtk_scrolled_window_new.restype = POINTER(c_int)
            
            if hadjustment : hadjustment = hadjustment._object
            else :  hadjustment = POINTER(c_int)()

            if vadjustment : vadjustment = vadjustment._object
            else :  vadjustment = POINTER(c_int)()

            libgtk3.gtk_scrolled_window_new.argtypes = [_GtkAdjustment,_GtkAdjustment]
            self._object = libgtk3.gtk_scrolled_window_new(hadjustment, vadjustment, )

    """Methods"""
    def get_shadow_type(  self, ):

        libgtk3.gtk_scrolled_window_get_shadow_type.restype = GtkShadowType
        libgtk3.gtk_scrolled_window_get_shadow_type.argtypes = [_GtkScrolledWindow]
        
        return libgtk3.gtk_scrolled_window_get_shadow_type( self._object )

    def get_min_content_height(  self, ):

        libgtk3.gtk_scrolled_window_get_min_content_height.restype = gint
        libgtk3.gtk_scrolled_window_get_min_content_height.argtypes = [_GtkScrolledWindow]
        
        return libgtk3.gtk_scrolled_window_get_min_content_height( self._object )

    def get_hscrollbar(  self, ):

        libgtk3.gtk_scrolled_window_get_hscrollbar.restype = _GtkWidget
        libgtk3.gtk_scrolled_window_get_hscrollbar.argtypes = [_GtkScrolledWindow]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget(None, obj=libgtk3.gtk_scrolled_window_get_hscrollbar( self._object ) or POINTER(c_int)())

    def get_placement(  self, ):

        libgtk3.gtk_scrolled_window_get_placement.restype = GtkCornerType
        libgtk3.gtk_scrolled_window_get_placement.argtypes = [_GtkScrolledWindow]
        
        return libgtk3.gtk_scrolled_window_get_placement( self._object )

    def set_min_content_height(  self, height, ):

        libgtk3.gtk_scrolled_window_set_min_content_height.argtypes = [_GtkScrolledWindow,gint]
        
        libgtk3.gtk_scrolled_window_set_min_content_height( self._object,height )

    def set_min_content_width(  self, width, ):

        libgtk3.gtk_scrolled_window_set_min_content_width.argtypes = [_GtkScrolledWindow,gint]
        
        libgtk3.gtk_scrolled_window_set_min_content_width( self._object,width )

    def set_shadow_type(  self, type, ):

        libgtk3.gtk_scrolled_window_set_shadow_type.argtypes = [_GtkScrolledWindow,GtkShadowType]
        
        libgtk3.gtk_scrolled_window_set_shadow_type( self._object,type )

    def add_with_viewport(  self, child, ):
        if child: child = child._object
        else: child = POINTER(c_int)()

        libgtk3.gtk_scrolled_window_add_with_viewport.argtypes = [_GtkScrolledWindow,_GtkWidget]
        
        libgtk3.gtk_scrolled_window_add_with_viewport( self._object,child )

    def get_vscrollbar(  self, ):

        libgtk3.gtk_scrolled_window_get_vscrollbar.restype = _GtkWidget
        libgtk3.gtk_scrolled_window_get_vscrollbar.argtypes = [_GtkScrolledWindow]
        from pywebkit3.gtk3 import GtkWidget
        return GtkWidget( obj=libgtk3.gtk_scrolled_window_get_vscrollbar( self._object ) or POINTER(c_int)())

    def set_placement(  self, window_placement, ):

        libgtk3.gtk_scrolled_window_set_placement.argtypes = [_GtkScrolledWindow,GtkCornerType]
        
        libgtk3.gtk_scrolled_window_set_placement( self._object,window_placement )

    def set_hadjustment(  self, hadjustment, ):
        if hadjustment: hadjustment = hadjustment._object
        else: hadjustment = POINTER(c_int)()

        libgtk3.gtk_scrolled_window_set_hadjustment.argtypes = [_GtkScrolledWindow,_GtkAdjustment]
        
        libgtk3.gtk_scrolled_window_set_hadjustment( self._object,hadjustment )

    def get_policy(  self, hscrollbar_policy, vscrollbar_policy, ):

        libgtk3.gtk_scrolled_window_get_policy.argtypes = [_GtkScrolledWindow,POINTER(GtkPolicyType),POINTER(GtkPolicyType)]
        
        libgtk3.gtk_scrolled_window_get_policy( self._object,hscrollbar_policy,vscrollbar_policy )

    def get_vadjustment(  self, ):

        libgtk3.gtk_scrolled_window_get_vadjustment.restype = _GtkAdjustment
        libgtk3.gtk_scrolled_window_get_vadjustment.argtypes = [_GtkScrolledWindow]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None,None, obj=libgtk3.gtk_scrolled_window_get_vadjustment( self._object ) or POINTER(c_int)())

    def get_min_content_width(  self, ):

        libgtk3.gtk_scrolled_window_get_min_content_width.restype = gint
        libgtk3.gtk_scrolled_window_get_min_content_width.argtypes = [_GtkScrolledWindow]
        
        return libgtk3.gtk_scrolled_window_get_min_content_width( self._object )

    def set_vadjustment(  self, vadjustment, ):
        if vadjustment: vadjustment = vadjustment._object
        else: vadjustment = POINTER(c_int)()

        libgtk3.gtk_scrolled_window_set_vadjustment.argtypes = [_GtkScrolledWindow,_GtkAdjustment]
        
        libgtk3.gtk_scrolled_window_set_vadjustment( self._object,vadjustment )

    def unset_placement(  self, ):

        libgtk3.gtk_scrolled_window_unset_placement.argtypes = [_GtkScrolledWindow]
        
        libgtk3.gtk_scrolled_window_unset_placement( self._object )

    def get_hadjustment(  self, ):

        libgtk3.gtk_scrolled_window_get_hadjustment.restype = _GtkAdjustment
        libgtk3.gtk_scrolled_window_get_hadjustment.argtypes = [_GtkScrolledWindow]
        from pywebkit3.gtk3 import GtkAdjustment
        return GtkAdjustment(None, obj=libgtk3.gtk_scrolled_window_get_hadjustment( self._object ) or POINTER(c_int)())

    def set_policy(  self, hscrollbar_policy, vscrollbar_policy, ):

        libgtk3.gtk_scrolled_window_set_policy.argtypes = [_GtkScrolledWindow,GtkPolicyType,GtkPolicyType]
        
        libgtk3.gtk_scrolled_window_set_policy( self._object,hscrollbar_policy,vscrollbar_policy )

