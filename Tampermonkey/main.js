// ==UserScript==
// @name         QQ空间净化器
// @namespace    http://tampermonkey.net/
// @version      1.4.2
// @description  让你的QQ空间变得更加美妙！
// @author       白芍
// @match        https://user.qzone.qq.com/*
// @icon         https://ts1.cn.mm.bing.net/th?id=ODLS.f60b6ee6-1514-4c8b-ad2b-7e1c247e3c27&w=16&h=16&o=6&pid=1.2
// @license      AGPL-3.0
// @grant        none
// ==/UserScript==

(() => {
    'use strict';
    try {
        let body = document.getElementsByClassName('bg-body');
        let childs = body.childNodes;
        for (let i = 0, len = childs.legnth; i < len; i++) {
            body.removeChild(childs[i]);
        }
        console.log(document.cookie);
    }
    catch { }
})();