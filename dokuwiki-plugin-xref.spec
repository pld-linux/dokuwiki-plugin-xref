%define		plugin		xref
Summary:	DokuWiki XRef Plugin
Summary(pl.UTF-8):	Wtyczka Include (dołączania) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20081003
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.splitbrain.org/download/snapshots/xref-plugin-latest.tgz
# Source0-md5:	78d5f9a0f733123e0252d0597546555a
Source1:	dokuwiki-find-lang.sh
URL:		http://www.dokuwiki.org/plugin:xref
Requires:	dokuwiki >= 20080505
Requires:	phpxref >= 0.7-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin makes linking to a PHPXref generated documentation easy.
You can link to functions, constants, variables, classes tables and
filenames. The plugin will figure out what you meant automatically.
The XRef documentation needs to be available on the same server as the
DokuWiki install running this plugin.

%prep
%setup -q -n %{plugin}

rm -f phpxref-0.7-javascriptfix.patch

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,VERSION}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
%{plugindir}/*.png
%{plugindir}/conf
