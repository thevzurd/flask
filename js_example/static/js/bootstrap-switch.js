/* ========================================================================
 * bootstrap-switch - v2.0.0
 * http://www.bootstrap-switch.org
 * ========================================================================
 * Copyright 2012-2013 Mattia Larentis
 *
 * ========================================================================
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================================
 */

(function(){!function(a){return a.fn.bootstrapSwitch=function(b){var c;return c={init:function(){return this.each(function(){var b,c,d,e,f,g,h,i;return c=a(this),f=a("<span>",{"class":"switch-left",html:function(){var a,b;return a="On",b=c.data("on-label"),null!=b&&(a=b),a}}),g=a("<span>",{"class":"switch-right",html:function(){var a,b;return a="Off",b=c.data("off-label"),null!=b&&(a=b),a}}),e=a("<label>",{"for":c.attr("id"),html:function(){var a,b,d;return a="&nbsp;",b=c.data("label-icon"),d=c.data("text-label"),null!=b&&(a='<i class="icon '+b+'"></i>'),null!=d&&(a=d),a}}),b=a("<div>"),h=a("<div>",{"class":"has-switch",tabindex:0}),d=c.closest("form"),i=function(){return e.hasClass("label-change-switch")?void 0:e.trigger("mousedown").trigger("mouseup").trigger("click")},c.data("bootstrap-switch",!0),c.attr("class")&&a.each(["switch-mini","switch-small","switch-large"],function(a,b){return c.attr("class").indexOf(b)>=0?(f.addClass(b),e.addClass(b),g.addClass(b)):void 0}),null!=c.data("on")&&f.addClass("switch-"+c.data("on")),null!=c.data("off")&&g.addClass("switch-"+c.data("off")),b.data("animated",!1),c.data("animated")!==!1&&b.addClass("switch-animate").data("animated",!0),b=c.wrap(b).parent(),h=b.wrap(h).parent(),c.before(f).before(e).before(g),b.addClass(c.is(":checked")?"switch-on":"switch-off"),(c.is(":disabled")||c.is("[readonly]"))&&h.addClass("disabled"),c.on("keydown",function(a){return 32===a.keyCode?(a.stopImmediatePropagation(),a.preventDefault(),i()):void 0}).on("change",function(a,d){var e,f;return e=c.is(":checked"),f=b.hasClass("switch-off"),a.preventDefault(),b.css("left",""),f!==e||(e?b.removeClass("switch-off").addClass("switch-on"):b.removeClass("switch-on").addClass("switch-off"),b.data("animated")!==!1&&b.addClass("switch-animate"),"boolean"==typeof d&&d)?void 0:c.trigger("switch-change",{el:c,value:e})}),h.on("keydown",function(a){if(a.which&&!c.is(":disabled")&&!c.is("[readonly]"))switch(a.which){case 32:return a.preventDefault(),i();case 37:if(a.preventDefault(),c.is(":checked"))return i();break;case 39:if(a.preventDefault(),!c.is(":checked"))return i()}}),f.on("click",function(){return i()}),g.on("click",function(){return i()}),e.on("mousedown touchstart",function(a){var d;return d=!1,a.preventDefault(),a.stopImmediatePropagation(),b.removeClass("switch-animate"),c.is(":disabled")||c.is("[readonly]")||c.hasClass("radio-no-uncheck")?e.unbind("click"):e.on("mousemove touchmove",function(a){var c,e,f,g;return f=(a.pageX||a.originalEvent.targetTouches[0].pageX)-h.offset().left,e=f/h.width()*100,c=25,g=75,d=!0,c>e?e=c:e>g&&(e=g),b.css("left",e-g+"%")}).on("click touchend",function(a){return a.stopImmediatePropagation(),a.preventDefault(),e.unbind("mouseleave"),d?c.prop("checked",parseInt(e.parent().css("left"),10)>-25):c.prop("checked",!c.is(":checked")),d=!1,c.trigger("change")}).on("mouseleave",function(a){return a.preventDefault(),a.stopImmediatePropagation(),e.unbind("mouseleave mousemove").trigger("mouseup"),c.prop("checked",parseInt(e.parent().css("left"),10)>-25).trigger("change")}).on("mouseup",function(a){return a.stopImmediatePropagation(),a.preventDefault(),e.trigger("mouseleave")})}),d.data("bootstrap-switch")?void 0:d.bind("reset",function(){return window.setTimeout(function(){return d.find(".has-switch").each(function(){var b;return b=a(this).find("input"),b.prop("checked",b.is(":checked")).trigger("change")})},1)}).data("bootstrap-switch",!0)})},setDisabled:function(b){var c,d;return c=a(this),d=c.parents(".has-switch"),b?(d.addClass("disabled"),c.prop("disabled",!0)):(d.removeClass("disabled"),c.prop("disabled",!1)),c},toggleDisabled:function(){var b;return b=a(this),b.prop("disabled",!b.is(":disabled")).parents(".has-switch").toggleClass("disabled"),b},isDisabled:function(){return a(this).is(":disabled")},setReadOnly:function(b){var c,d;return c=a(this),d=c.parents(".has-switch"),b?(d.addClass("disabled"),c.prop("readonly",!0)):(d.removeClass("disabled"),c.prop("readonly",!1)),c},toggleReadOnly:function(){var b;return b=a(this),b.prop("readonly",!b.is("[readonly]")).parents(".has-switch").toggleClass("disabled"),b},isReadOnly:function(){return a(this).is("[readonly]")},toggleState:function(b){var c;return c=a(this),c.prop("checked",!c.is(":checked")).trigger("change",b),c},toggleRadioState:function(b){var c;return c=a(this),c.not(":checked").prop("checked",!c.is(":checked")).trigger("change",b),c},toggleRadioStateAllowUncheck:function(b,c){var d;return d=a(this),b?d.not(":checked").trigger("change",c):d.not(":checked").prop("checked",!d.is(":checked")).trigger("change",c),d},setState:function(b,c){var d;return d=a(this),d.prop("checked",b).trigger("change",c),d},setOnLabel:function(b){var c;return c=a(this),c.siblings(".switch-left").html(b),c},setOffLabel:function(b){var c;return c=a(this),c.siblings(".switch-right").html(b),c},setOnClass:function(b){var c,d,e;return c=a(this),d=c.siblings(".switch-left"),e=c.attr("data-on"),null!=b?(null!=e&&d.removeClass("switch-"+e),d.addClass("switch-"+b),c):void 0},setOffClass:function(b){var c,d,e;return c=a(this),d=c.siblings(".switch-right"),e=c.attr("data-off"),null!=b?(null!=e&&d.removeClass("switch-"+e),d.addClass("switch-"+b),c):void 0},setAnimated:function(b){var c,d;return d=a(this),c=d.parent(),null==b&&(b=!1),c.data("animated",b).attr("data-animated",b)[c.data("animated")!==!1?"addClass":"removeClass"]("switch-animate"),d},setSizeClass:function(b){var c,d,e,f;return c=a(this),e=c.siblings(".switch-left"),d=c.siblings("label"),f=c.siblings(".switch-right"),a.each(["switch-mini","switch-small","switch-large"],function(a,c){return c!==b?(e.removeClass(c),d.removeClass(c),f.removeClass(c)):(e.addClass(c),d.addClass(c),f.addClass(c))}),c},setTextLabel:function(b){var c;return c=a(this),c.siblings("label").html(b||"&nbsp"),c},setTextIcon:function(b){var c;return c=a(this),c.siblings("label").html(b?'<i class="icon '+b+'"></i>':"&nbsp;"),c},state:function(){return a(this).is(":checked")},destroy:function(){var b,c,d;return c=a(this),b=c.parent(),d=b.closest("form"),b.children().not(c).remove(),c.unwrap().unwrap().unbind("change"),d.length&&d.unbind("reset").removeData("bootstrapSwitch"),c}},c[b]?c[b].apply(this,Array.prototype.slice.call(arguments,1)):"object"!=typeof b&&b?a.error("Method "+b+" does not exist!"):c.init.apply(this,arguments)},this}(jQuery)}).call(this);
