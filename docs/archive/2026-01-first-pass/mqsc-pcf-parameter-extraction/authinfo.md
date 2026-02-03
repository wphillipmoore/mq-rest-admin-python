# MQSC to PCF parameter extraction: Authinfo

## Table of Contents

- [Purpose](#purpose)
- [First-run extraction](#first-run-extraction)
- [Authinfo command re-parse](#authinfo-command-re-parse)

## Purpose

Collect MQSC and PCF parameter mappings for authinfo commands, split from the first-run extraction to keep each qualifier readable.

## First-run extraction

```yaml
version: 1
generated_at: 2026-01-11T23:40:29Z
commands:
  - mqsc:
      name: ALTER AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085140_.html
      positional_parameters:
        - LDAP class user
        - LDAP password
        - LDAP user
        - Responder URL
        - base DN
        - connection name
        - delay time
        - name
        - qmgr-name
        - string
        - user field
        - user name
      input_parameters:
        - ADOPTCTX
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CMDSCOPE
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - NESTGRP
        - OCSPURL
        - QSGDISP
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER AUTHINFO':
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - QSGDISP
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_CHANGE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: null
      request_parameters: []
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - QSGDISP
          - SECCOMM
          - SHORTUSR
          - USRFIELD
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DEFINE AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085490_.html
      positional_parameters:
        - LDAP class name
        - LDAP field name
        - LDAP password
        - LDAP user
        - Responder URL
        - authinfo-name
        - base DN
        - connection name
        - delay time
        - name
        - qmgr-name
        - string
        - user name
      input_parameters:
        - ADOPTCTX
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CMDSCOPE
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - LIKE
        - NESTGRP
        - NOREPLACE
        - OCSPURL
        - QSGDISP
        - REPLACE
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE AUTHINFO':
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - LIKE
          - NESTGRP
          - NOREPLACE
          - OCSPURL
          - QSGDISP
          - REPLACE
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_CREATE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refdev/q091020_.html
      response_href: null
      request_parameters: []
      response_parameters: []
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - LIKE
          - NESTGRP
          - NOREPLACE
          - OCSPURL
          - QSGDISP
          - REPLACE
          - SECCOMM
          - SHORTUSR
          - USRFIELD
        pcf_unmapped: []
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped: []
    notes: []
  - mqsc:
      name: DELETE AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085780_.html
      positional_parameters:
        - name
        - qmgr-name
      input_parameters:
        - CMDSCOPE
        - IGNSTATE
        - QSGDISP
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE AUTHINFO':
          - CMDSCOPE
          - IGNSTATE
          - QSGDISP
    pcf:
      command: MQCMD_DELETE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087090_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087090_.html
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
      response_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          IGNSTATE:
            - IgnoreState
        unmapped:
          - CMDSCOPE
          - QSGDISP
        pcf_unmapped:
          - AuthInfoName
          - CommandScope
          - IgnoreState
          - QSGDisposition
      response:
        suggested:
          {}
        ambiguous:
          {}
        unmapped: []
        pcf_unmapped:
          - AuthInfoName
          - CommandScope
          - IgnoreState
          - QSGDisposition
    notes: []
  - mqsc:
      name: DISPLAY AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085990_.html
      positional_parameters:
        - generic-authentication-information-object-name
        - qmgr-name
      input_parameters:
        - ALL
        - AUTHTYPE
        - CMDSCOPE
        - QSGDISP
        - WHERE
      output_parameters:
        - ADOPTCTX
        - ALL
        - ALTDATE
        - ALTTIME
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - NESTGRP
        - OCSPURL
        - QSGDISP
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      section_sources:
        'Parameter descriptions for DISPLAY AUTHINFO':
          - ALL
          - AUTHTYPE
          - CMDSCOPE
          - QSGDISP
          - WHERE
        'Requested parameters':
          - ADOPTCTX
          - ALTDATE
          - ALTTIME
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_INQUIRE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087270_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087280_.html
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIA_ADOPT_CONTEXT
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_AUTH_INFO_DESC
            - MQCA_AUTH_INFO_NAME
            - MQIA_AUTH_INFO_TYPE
            - MQCA_AUTH_INFO_CONN_NAME
            - MQIA_AUTHENTICATION_FAIL_DELAY
            - MQIA_AUTHENTICATION_METHOD
            - MQIA_CHECK_CLIENT_BINDING
            - MQIA_CHECK_LOCAL_BINDING
            - MQIA_LDAP_AUTHORMD
            - MQCA_LDAP_BASE_DN_GROUPS
            - MQCA_LDAP_BASE_DN_USERS
            - MQCA_LDAP_FIND_GROUP_FIELD
            - MQCA_LDAP_GROUP_ATTR_FIELD
            - MQCA_LDAP_GROUP_OBJECT_CLASS
            - MQIA_LDAP_NESTGRP
            - MQCA_LDAP_PASSWORD
            - MQIA_LDAP_SECURE_COMM
            - MQCA_LDAP_SHORT_USER_FIELD
            - MQCA_LDAP_USER_ATTR_FIELD
            - MQCA_LDAP_USER_NAME
            - MQCA_LDAP_USER_OBJECT_CLASS
            - MQCA_AUTH_INFO_OCSP_URL
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
            - MQAIT_ALL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_LIVE
            - MQQSGD_ALL
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_PRIVATE
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoConnName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoDesc
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
        - name: AuthenticationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHENTICATE_OS
            - MQAUTHENTICATE_PAM
        - name: AuthorizationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_AUTHORMD_OS
            - MQLDAP_AUTHORMD_SEARCHGRP
            - MQLDAP_AUTHORMD_SEARCHUSER
            - MQLDAP_AUTHORMD_SRCHGRPSN
        - name: BaseDNGroup
          pcf_type: MQCFST
          type_hint: str
        - name: BaseDNUser
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: ClassGroup
          pcf_type: MQCFST
          type_hint: str
        - name: Classuser
          pcf_type: MQCFST
          type_hint: str
        - name: FailureDelay
          pcf_type: MQCFIN
          type_hint: int
        - name: FindGroup
          pcf_type: MQCFST
          type_hint: str
        - name: GroupField
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNesting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_NESTGRP_NO
            - MQLDAP_NESTGRP_YES
        - name: LDAPPassword
          pcf_type: MQCFST
          type_hint: str
        - name: LDAPUserName
          pcf_type: MQCFST
          type_hint: str
        - name: OCSPResponderURL
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: SecureComms
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortUser
          pcf_type: MQCFST
          type_hint: str
        - name: UserField
          pcf_type: MQCFST
          type_hint: str
    mapping:
      request:
        suggested:
          {}
        ambiguous:
          {}
        unmapped:
          - ALL
          - AUTHTYPE
          - CMDSCOPE
          - QSGDISP
          - WHERE
        pcf_unmapped:
          - AuthInfoAttrs
          - AuthInfoName
          - AuthInfoType
          - CommandScope
          - IntegerFilterCommand
          - QSGDisposition
          - StringFilterCommand
      response:
        suggested:
          CLASSUSR: Classuser
          SHORTUSR: ShortUser
          USRFIELD: UserField
        ambiguous:
          BASEDNU:
            - BaseDNUser
          CLASSGRP:
            - ClassGroup
          FINDGRP:
            - FindGroup
          GRPFIELD:
            - GroupField
        unmapped:
          - ADOPTCTX
          - ALTDATE
          - ALTTIME
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - CHCKCLNT
          - CHCKLOCL
          - CONNAME
          - DESCR
          - FAILDLAY
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - SECCOMM
        pcf_unmapped:
          - AlterationDate
          - AlterationTime
          - AuthInfoConnName
          - AuthInfoDesc
          - AuthInfoName
          - AuthInfoType
          - AuthenticationMethod
          - AuthorizationMethod
          - BaseDNGroup
          - BaseDNUser
          - ClassGroup
          - FailureDelay
          - FindGroup
          - GroupField
          - GroupNesting
          - LDAPPassword
          - LDAPUserName
          - OCSPResponderURL
          - QSGDisposition
          - SecureComms
    notes:
      - display-parameter-descriptions-treated-as-input
```

## Authinfo command re-parse

This addendum isolates corrected MQSC and PCF parameter sets. It is intentionally separate from the first-run extraction above and omits mapping heuristics.

```yaml
version: 1
generated_at: 2026-01-12T20:52:18Z
commands:
  - mqsc:
      name: ALTER AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085140_.html
      positional_parameters:
        - (name)
      input_parameters:
        - ADOPTCTX
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CMDSCOPE
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - NESTGRP
        - OCSPURL
        - QSGDISP
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      output_parameters: []
      section_sources:
        'Parameter descriptions for ALTER AUTHINFO':
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - QSGDISP
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_CHANGE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q086910_.html
      response_href: null
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
        - name: AdoptContext
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADPCTX_YES
            - MQADPCTX_NO
        - name: AuthInfoConnName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoDesc
          pcf_type: MQCFST
          type_hint: str
        - name: AuthenticationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHENTICATE_OS
            - MQAUTHENTICATE_PAM
        - name: AuthorizationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_AUTHORMD_OS
            - MQLDAP_AUTHORMD_SEARCHGRP
            - MQLDAP_AUTHORMD_SEARCHUSR
            - MQLDAP_AUTHORMD_SRCHGRPSN
        - name: BaseDNGroup
          pcf_type: MQCFST
          type_hint: str
        - name: BaseDNUser
          pcf_type: MQCFST
          type_hint: str
        - name: Checkclient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: Checklocal
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: ClassGroup
          pcf_type: MQCFST
          type_hint: str
        - name: Classuser
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: FailureDelay
          pcf_type: MQCFIN
          type_hint: int
        - name: FindGroup
          pcf_type: MQCFST
          type_hint: str
        - name: GroupField
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNesting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_NESTGRP_NO
            - MQLDAP_NESTGRP_YES
        - name: LDAPPassword
          pcf_type: MQCFST
          type_hint: str
        - name: LDAPUserName
          pcf_type: MQCFST
          type_hint: str
        - name: OCSPResponderURL
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_Q_MGR
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecureComms
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECCOMM_YES
            - MQSECCOMM_ANON
            - MQSECCOMM_NO
        - name: ShortUser
          pcf_type: MQCFST
          type_hint: str
        - name: UserField
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - change-authinfo-excludes-copy-only-parameters
  - mqsc:
      name: DEFINE AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085490_.html
      positional_parameters:
        - (name)
      input_parameters:
        - ADOPTCTX
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CMDSCOPE
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - LIKE
        - NESTGRP
        - OCSPURL
        - QSGDISP
        - REPLACE
        - NOREPLACE
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      output_parameters: []
      section_sources:
        'Parameter descriptions for DEFINE AUTHINFO':
          - ADOPTCTX
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CMDSCOPE
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - LIKE
          - NESTGRP
          - OCSPURL
          - QSGDISP
          - REPLACE
          - NOREPLACE
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_CREATE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q086910_.html
      response_href: null
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
        - name: AdoptContext
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQADPCTX_YES
            - MQADPCTX_NO
        - name: AuthInfoConnName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoDesc
          pcf_type: MQCFST
          type_hint: str
        - name: AuthenticationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHENTICATE_OS
            - MQAUTHENTICATE_PAM
        - name: AuthorizationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_AUTHORMD_OS
            - MQLDAP_AUTHORMD_SEARCHGRP
            - MQLDAP_AUTHORMD_SEARCHUSR
            - MQLDAP_AUTHORMD_SRCHGRPSN
        - name: BaseDNGroup
          pcf_type: MQCFST
          type_hint: str
        - name: BaseDNUser
          pcf_type: MQCFST
          type_hint: str
        - name: Checkclient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: Checklocal
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: ClassGroup
          pcf_type: MQCFST
          type_hint: str
        - name: Classuser
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: FailureDelay
          pcf_type: MQCFIN
          type_hint: int
        - name: FindGroup
          pcf_type: MQCFST
          type_hint: str
        - name: GroupField
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNesting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_NESTGRP_NO
            - MQLDAP_NESTGRP_YES
        - name: LDAPPassword
          pcf_type: MQCFST
          type_hint: str
        - name: LDAPUserName
          pcf_type: MQCFST
          type_hint: str
        - name: OCSPResponderURL
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_PRIVATE
            - MQQSGD_Q_MGR
        - name: Replace
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQRP_YES
            - MQRP_NO
        - name: SecureComms
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQSECCOMM_YES
            - MQSECCOMM_ANON
            - MQSECCOMM_NO
        - name: ShortUser
          pcf_type: MQCFST
          type_hint: str
        - name: UserField
          pcf_type: MQCFST
          type_hint: str
      response_parameters: []
    notes:
      - create-authinfo-excludes-copy-only-parameters
  - mqsc:
      name: DELETE AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085780_.html
      positional_parameters:
        - (name)
      input_parameters:
        - CMDSCOPE
        - QSGDISP
        - IGNSTATE
      output_parameters: []
      section_sources:
        'Parameter descriptions for DELETE AUTHINFO':
          - CMDSCOPE
          - QSGDISP
          - IGNSTATE
    pcf:
      command: MQCMD_DELETE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087090_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087090_.html
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQIS_NO
            - MQIS_YES
      response_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: IgnoreState
          pcf_type: MQCFST
          type_hint: str
          enum_values:
            - MQIS_YES
            - MQIS_NO
    notes:
      - ignore-state-type-inferred-from-mqsc-ignstate
      - ignore-state-name-normalized
  - mqsc:
      name: DISPLAY AUTHINFO
      href: SSFKSJ_9.4.0/refadmin/q085990_.html
      positional_parameters:
        - (generic-authentication-information-object-name)
      input_parameters:
        - ALL
        - AUTHTYPE
        - CMDSCOPE
        - QSGDISP
        - WHERE
      output_parameters:
        - ADOPTCTX
        - ALTDATE
        - ALTTIME
        - AUTHENMD
        - AUTHORMD
        - AUTHTYPE
        - BASEDNG
        - BASEDNU
        - CHCKCLNT
        - CHCKLOCL
        - CLASSGRP
        - CLASSUSR
        - CONNAME
        - DESCR
        - FAILDLAY
        - FINDGRP
        - GRPFIELD
        - LDAPPWD
        - LDAPUSER
        - NESTGRP
        - OCSPURL
        - SECCOMM
        - SHORTUSR
        - USRFIELD
      section_sources:
        'Parameter descriptions for DISPLAY AUTHINFO':
          - ALL
          - AUTHTYPE
          - CMDSCOPE
          - QSGDISP
          - WHERE
        'Requested parameters':
          - ADOPTCTX
          - ALTDATE
          - ALTTIME
          - AUTHENMD
          - AUTHORMD
          - AUTHTYPE
          - BASEDNG
          - BASEDNU
          - CHCKCLNT
          - CHCKLOCL
          - CLASSGRP
          - CLASSUSR
          - CONNAME
          - DESCR
          - FAILDLAY
          - FINDGRP
          - GRPFIELD
          - LDAPPWD
          - LDAPUSER
          - NESTGRP
          - OCSPURL
          - SECCOMM
          - SHORTUSR
          - USRFIELD
    pcf:
      command: MQCMD_INQUIRE_AUTH_INFO
      request_href: SSFKSJ_9.4.0/refadmin/q087270_.html
      response_href: SSFKSJ_9.4.0/refadmin/q087280_.html
      request_parameters:
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoAttrs
          pcf_type: MQCFIL
          type_hint: int
          enum_values:
            - MQIACF_ALL
            - MQIA_ADOPT_CONTEXT
            - MQCA_ALTERATION_DATE
            - MQCA_ALTERATION_TIME
            - MQCA_AUTH_INFO_DESC
            - MQCA_AUTH_INFO_NAME
            - MQIA_AUTH_INFO_TYPE
            - MQCA_AUTH_INFO_CONN_NAME
            - MQIA_AUTHENTICATION_FAIL_DELAY
            - MQIA_AUTHENTICATION_METHOD
            - MQIA_CHECK_CLIENT_BINDING
            - MQIA_CHECK_LOCAL_BINDING
            - MQIA_LDAP_AUTHORMD
            - MQCA_LDAP_BASE_DN_GROUPS
            - MQCA_LDAP_BASE_DN_USERS
            - MQCA_LDAP_FIND_GROUP_FIELD
            - MQCA_LDAP_GROUP_ATTR_FIELD
            - MQCA_LDAP_GROUP_OBJECT_CLASS
            - MQIA_LDAP_NESTGRP
            - MQCA_LDAP_PASSWORD
            - MQIA_LDAP_SECURE_COMM
            - MQCA_LDAP_SHORT_USER_FIELD
            - MQCA_LDAP_USER_ATTR_FIELD
            - MQCA_LDAP_USER_NAME
            - MQCA_LDAP_USER_OBJECT_CLASS
            - MQCA_AUTH_INFO_OCSP_URL
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
            - MQAIT_ALL
        - name: CommandScope
          pcf_type: MQCFST
          type_hint: str
        - name: IntegerFilterCommand
          pcf_type: MQCFIF
          type_hint: null
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_LIVE
            - MQQSGD_ALL
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
            - MQQSGD_PRIVATE
        - name: StringFilterCommand
          pcf_type: MQCFSF
          type_hint: null
      response_parameters:
        - name: AlterationDate
          pcf_type: MQCFST
          type_hint: str
        - name: AlterationTime
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoConnName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoDesc
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoName
          pcf_type: MQCFST
          type_hint: str
        - name: AuthInfoType
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAIT_CRL_LDAP
            - MQAIT_OCSP
            - MQAIT_IDPW_OS
            - MQAIT_IDPW_LDAP
        - name: AuthenticationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQAUTHENTICATE_OS
            - MQAUTHENTICATE_PAM
        - name: AuthorizationMethod
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_AUTHORMD_OS
            - MQLDAP_AUTHORMD_SEARCHGRP
            - MQLDAP_AUTHORMD_SEARCHUSER
            - MQLDAP_AUTHORMD_SRCHGRPSN
        - name: BaseDNGroup
          pcf_type: MQCFST
          type_hint: str
        - name: BaseDNUser
          pcf_type: MQCFST
          type_hint: str
        - name: Checklocal
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: Checkclient
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQCHK_NONE
            - MQCHK_OPTIONAL
            - MQCHK_REQUIRED
            - MQCHK_REQUIRED_ADMIN
        - name: ClassGroup
          pcf_type: MQCFST
          type_hint: str
        - name: Classuser
          pcf_type: MQCFST
          type_hint: str
        - name: FailureDelay
          pcf_type: MQCFIN
          type_hint: int
        - name: FindGroup
          pcf_type: MQCFST
          type_hint: str
        - name: GroupField
          pcf_type: MQCFST
          type_hint: str
        - name: GroupNesting
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQLDAP_NESTGRP_NO
            - MQLDAP_NESTGRP_YES
        - name: LDAPPassword
          pcf_type: MQCFST
          type_hint: str
        - name: LDAPUserName
          pcf_type: MQCFST
          type_hint: str
        - name: OCSPResponderURL
          pcf_type: MQCFST
          type_hint: str
        - name: QSGDisposition
          pcf_type: MQCFIN
          type_hint: int
          enum_values:
            - MQQSGD_COPY
            - MQQSGD_GROUP
            - MQQSGD_Q_MGR
        - name: SecureComms
          pcf_type: MQCFIN
          type_hint: int
        - name: ShortUser
          pcf_type: MQCFST
          type_hint: str
        - name: UserField
          pcf_type: MQCFST
          type_hint: str
    notes:
      - qsgdisposition-returned-on-zos-only
      - authormd-searchuser-spelling-differs-from-change-create-docs
```

## Output-parameter refresh

```yaml
version: 1
generated_at: 2026-02-02T19:46:59Z
commands:
  - name: DISPLAY AUTHINFO
    output_parameters:
      - ADOPTCTX
      - ALL
      - ALTDATE
      - ALTTIME
      - AUTHENMD
      - AUTHORMD
      - AUTHTYPE
      - BASEDNG
      - BASEDNU
      - CHCKCLNT
      - CHCKLOCL
      - CLASSGRP
      - CLASSUSR
      - CONNAME
      - DESCR
      - FAILDLAY
      - FINDGRP
      - GRPFIELD
      - LDAPPWD
      - LDAPUSER
      - NESTGRP
      - OCSPURL
      - QSGDISP
      - SECCOMM
      - SHORTUSR
      - USRFIELD
```
