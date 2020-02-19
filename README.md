# apisix_admin

```shell
功能说明:
  1. apisix 后台管理, 用python作为中间层, 前端UI调用python， 支持多集群管理和AD域账号认证, 组件细粒度权限控制待完成
  2. apisix-admin的接口完全兼容apisix的接口，新增了多集群管理和AD认证, 用户权限等功能。
    Tenant 是多个apisix集群管理模块
    Users 是用户管理模块

开发环境说明:
  把settings.py里的APISIX_DEV_URL这个变量硬编码成APIsix的IP地址， 同时把DEFAULT_PERMISSION_CLASSES注释掉即可。




```
