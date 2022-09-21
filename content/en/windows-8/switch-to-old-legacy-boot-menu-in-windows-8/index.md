+++
title="Switch To Old Boot Menu In Windows 8"
summary="Speed up windows 8 Loading time by Switching to old legacy boot menu in windows 8.And also you can speed up boot process in windows 8 by old legacy boot menu."
keywords=["windows 8 speed secrets,legacy boot menu windows8,windows8,windows 8"
]
type='post'
date='2019-09-24T18:07:21+0000'
lastmod='2019-09-24T18:07:21+0000'
draft='false'
contributors= ["Arun Gudelli"]
images=[]
[image]
caption='Switch To Old Boot Menu In Windows 8'
focal_point=''
preview_only=false
+++

This post will explains how to switch to old boot menu in window8

Windows 8 Metro boot menu has very good Graphical user interface, which is both touch and mouse friendly.We can boot the OS of our choice easily.

The reason behind this Metro style Boot menu is to support Windows tablets which don’t have hardware keyboard.But if your using desktop this metro style boot menu can cause some issues

### <em>The Problem with Metro Style boot Menu:</em>

The problem with the new boot manager is that it’s Graphical and requires Windows 8 to load of all the drivers(such as touch and mouse drivers) required to show the graphical screen.This may delay the boot process.

If you select Windows 8 it continues booting from that point and Windows 8 starts quickly.

But If you pick another OS (such as Ubuntu,Windows 7),it reboots again,and start the selected OS in next boot.This will take a lot of time on old computers.

### <em>Switch to Legacy Boot Manager:</em>

Getting back to legacy old boot menu is very simple.

<ul><li>Open command prompt in admin mode.</li><li>Enter the following command.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #000000;"><em>bcdedit /set {default} bootmenupolicy legacy</em></span></li><li>To bring back Metro style boot menu. &nbsp; &nbsp; &nbsp;<em>bcdedit /set {default} bootmenupolicy standard</em></li></ul>

Now it will load in text based boot menu as in previous versions of windows.

If you are using dual booting this saves lot of &nbsp;time.













