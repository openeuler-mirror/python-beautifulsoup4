%global _empty_manifest_terminate_build 0
Name:           python-beautifulsoup4
Version:        4.11.1
Release:        1
Summary:        Screen-scraping library
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source0:        https://files.pythonhosted.org/packages/e8/b0/cd2b968000577ec5ce6c741a54d846dfa402372369b8b6861720aa9ecea7/beautifulsoup4-4.11.1.tar.gz
BuildArch:      noarch

Requires:	python3-soupsieve

%description
This package provides a python library which is designed for quick
turnaround projects.It provides methods for navigating and modifying
a parse tree.It can help convert incoming documents to Unicode
and outgoing documents to utf-8.

%package -n python3-beautifulsoup4
Summary:        Screen-scraping library
Provides:       python-beautifulsoup4
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-html5lib
BuildRequires:  python3-lxml
BuildRequires:  python3-pip
%description -n python3-beautifulsoup4
This package provides a python library which is designed for quick
turnaround projects.It provides methods for navigating and modifying
a parse tree.It can help convert incoming documents to Unicode
and outgoing documents to utf-8.

%package help
Summary:        Screen-scraping library
Provides:       python3-beautifulsoup4-doc
%description help
This package provides a python library which is designed for quick
turnaround projects.It provides methods for navigating and modifying
a parse tree.It can help convert incoming documents to Unicode
and outgoing documents to utf-8.

%prep
%autosetup -n beautifulsoup4-%{version}

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-beautifulsoup4 -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Thu Nov 10 2022 liqiuyu <liqiuyu@kylinos.cn> - 4.11.1-1
- Upgrade package to version 4.11.1

* Tue May 24 2022 renliang <renliang@uniontech.com> - 4.10.0-1
- Upgrade package python3-beautifulsoup4 to version 4.10.0

* Mon Jan 10 2022 shixuantong <shixuantong@huawei.com> - 4.9.3-2
- converts the code base to Python 3, and removes the use_2to3 reference in setup.py.

* Mon Jul 26 2021 liusheng<liusheng2048@huawei.com>  - 4.9.3-1
- Upgrade to version 4.9.3

* Fri Oct 30 2020 wangjie<wangjie294@huawei.com> -4.6.3-4
- Type:NA
- ID:NA
- SUG:NA
- DESC:remove python2
* Tue Aug 4 2020 wenzhanli<wenzhanli2@huawei.com> - 4.6.3-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix make test error

* Sat Sep 21 2019 yangfeiyu <yangfeiyu2@huawei.com> - 4.6.3-2
- spec init
