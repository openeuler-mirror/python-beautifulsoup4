Name:           python-beautifulsoup4
Version:        4.6.3
Release:        4
Summary:        HTML/XML parser for quick-turnaround projects
License:        MIT
URL:            http://www.crummy.com/software/BeautifulSoup/
Source0:        https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel python3-html5lib python3-setuptools python3-lxml

%global _description\
This package provides a python library which is designed for quick\
turnaround projects.It provides methods for navigating and modifying\
a parse tree.It can help convert incoming documents to Unicode\
and outgoing documents to utf-8.

%description %_description

%package     -n python3-beautifulsoup4
Summary:        %summary
%description -n python3-beautifulsoup4 %_description
Obsoletes:      python3-BeautifulSoup < 1:3.2.1-2
Requires:       python3-lxml

%prep
%setup -q -n beautifulsoup4-%{version}
mv AUTHORS.txt AUTHORS.txt.iso
iconv -f ISO-8859-1 -t UTF-8 -o AUTHORS.txt AUTHORS.txt.iso
touch -r AUTHORS.txt.iso AUTHORS.txt
rm -rf %{py3dir} 
cp -a . %{py3dir}

%build
pushd %{py3dir}
2to3 --write --nobackups .
%{py3_build}

%install
pushd %{py3dir}
%{py3_install}

%check
pushd %{py3dir}
%{__python3} -m unittest discover -s bs4 || :

%files -n python3-beautifulsoup4
%{python3_sitelib}/bs4
%{python3_sitelib}/beautifulsoup4-%{version}*.egg-info
%doc TODO.txt AUTHORS.txt NEWS.txt
%license COPYING.txt

%changelog
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
