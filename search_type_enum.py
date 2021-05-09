from enum import Enum


class search_type(Enum):
    OPEN_FTP_SERVER = 'inurl:ftp intitle:index of'
    SSH_PRIVATE_KEY = 'intitle:index.of id_rsa -id_rsa.pub'
    ENV_FILES = 'DB_USERNAME filetype:env'
    VULN_WEB_SERVER = 'inurl:/proc/self/cwd'
    LOG_FILES = 'allintext:username filetype:log'
    EMAIL_LIST = 'filetype:xls inurl:"email.xls"'
    ZOOM_MEETINGS = 'inurl:zoom.us/j and intext:scheduled for'
    WORDPRESS_ADMIN = 'intitle:"Index of" wp-admin'
    APACHE2 = 'intitle:"Apache2 Ubuntu Default Page: It works"'
    PHPMYADMIN = '"Index of" inurl:phpmyadmin'
    JIRA = 'inurl:Dashboard.jspa intext:"Atlassian Jira Project Management Software"'
    KIBANA = 'inurl:app/kibana intext:Loading Kibana'
    GOV_RESTRICTED_DOC = 'allintitle: restricted filetype:doc site:gov'