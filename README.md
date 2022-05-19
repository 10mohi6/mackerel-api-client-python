# mackerel.api

[![PyPI](https://img.shields.io/pypi/v/mackerel.api)](https://pypi.org/project/mackerel.api/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/10mohi6/mackerel-api-client-python/branch/main/graph/badge.svg?token=ODOV9LETK1)](https://codecov.io/gh/10mohi6/mackerel-api-client-python)
[![Build Status](https://travis-ci.com/10mohi6/mackerel-api-client-python.svg?branch=main)](https://travis-ci.com/10mohi6/mackerel-api-client-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mackerel-api-client)](https://pypi.org/project/mackerel-api-client/)
[![Downloads](https://pepy.tech/badge/mackerel-api-client)](https://pepy.tech/project/mackerel-api-client)

mackerel.api is a python library for mackerel api on Python 3.6 and above.

## Install

    $ pip install mackerel.api

## Usage

```python
from mackerel.api import Client

client = Client("<mackerel api key>")
res = client.get("/org")
print(res.status_code, res.json())
```

## API

[documentation](https://mackerel.io/ja/api-docs/)

### service

```python
# サービスの一覧
client.get("/services")
# サービスの登録
client.post("/services", {"name": "<serviceName>, … "})
# サービスの削除
client.delete("/services/<serviceName>")
# ロールの一覧
client.get("/services/<serviceName>/roles")
# ロールの登録
client.post("/services/<serviceName>/roles", {"name": "<serviceName>, … "})
# ロールの削除
client.delete("/services/<serviceName>/roles/<roleName>")
# メトリック名の一覧
client.get("/services/<serviceName>/metric-names")
```

### host

```python
# ホストの登録
client.post("/hosts", {"name": "<hostName>", … })
# ホスト情報の取得
client.get("/hosts/<hostId>")
# ホスト情報の更新
client.put("/hosts/<hostId>", {"name": "<hostName>", … })
# ホストのステータスの更新
client.post("/hosts/<hostId>/status", {"status": "<hostStatus>"})
# ホストのロールの更新
client.put("/hosts/<hostId>/role-fullnames", {"roleFullnames": [ <string>, <string>, … ]})
# ホストの退役
client.post("/hosts/<hostId>/retire", {})
# ホストの一覧
client.get("/hosts")
# メトリック名の一覧
client.get("/hosts/<hostId>/metric-names")
# 監視ステータスの一覧
client.get("/hosts/<hostId>/monitored-statuses")
```

### host metric

```python
# メトリックの投稿
client.post("/tsdb", [ <metricValue>, <metricValue>, … ])
# ホストのメトリックの値の取得
client.get("/hosts/<hostId>/metrics", {"name": "<metricName>", … })
# メトリックの最新値の取得
client.get("/tsdb/latest", {"hostId": "<hostId>", … })
# グラフ定義の投稿
client.post("/graph-defs/create", [ <graphDef>, <graphDef>, … ])
```

### service metric

```python
# サービスメトリックの投稿
client.post("/services/<serviceName>/tsdb", [ <metricValue>, <metricValue>, … ])
# サービスメトリックの値の取得
client.get("/services/<serviceName>/metrics", {"name": "<serviceName>", … })
```

### check

```python
# チェック監視結果の投稿
client.post("/monitoring/checks/report", {"reports": [ <report>, <report>, … ]})
```

### metadata

```python
# ホストメタデータの取得
client.get("/hosts/<hostId>/metadata/<namespace>")
# ホストメタデータの登録・更新
client.put("/hosts/<hostId>/metadata/<namespace>", { … })
# ホストメタデータの削除
client.delete("/hosts/<hostId>/metadata/<namespace>")
# ホストメタデータの一覧
client.get("/hosts/<hostId>/metadata")
# サービスメタデータの取得
client.get("/services/<serviceName>/metadata/<namespace>")
# サービスメタデータの登録・更新
client.put("/services/<serviceName>/metadata/<namespace>", { … })
# サービスメタデータの削除
client.delete("services/<serviceName>/metadata/<namespace>")
# サービスメタデータの一覧
client.get("/services/<serviceName>/metadata")
# ロールメタデータの取得
client.get("/services/<serviceName>/roles/<roleName>/metadata/<namespace>")
# ロールメタデータの登録・更新
client.put("/services/<serviceName>/roles/<roleName>/metadata/<namespace>", { … })
# ロールメタデータの削除
client.delete("/services/<serviceName>/roles/<roleName>/metadata/<namespace>")
# ロールメタデータの一覧
client.get("/services/<serviceName>/roles/<roleName>/metadata")
```

### monitor

```python
# 監視ルールの登録
client.post("/monitors", {"type": "host", … })
# 監視ルールの一覧
client.get("/monitors")
# 監視ルールの取得
client.get("/monitors/<monitorId>")
# 監視ルールの更新
client.put("/monitors/<monitorId>", { … })
# 監視ルールの削除
client.delete("/monitors/<monitorId>")
```

### downtime

```python
# ダウンタイムの登録
client.post("/downtimes", {"name": "<downtimeName>", … })
# ダウンタイムの一覧
client.get("/downtimes")
# ダウンタイムの更新
client.put("/downtimes/<downtimeId>", {"name": "<downtimeName>", … })
# ダウンタイムの削除
client.delete("/downtimes/<downtimeId>")
```

### channel

```python
# 通知チャンネルの一覧
client.get("/channels")
# 通知チャンネルの登録
client.post("/channels", {"type": "email", … })
# 通知チャンネルの削除
client.delete("/channels/<channelId>")
```

### group

```python
# 通知グループの登録
client.post("/notification-groups", {"name": "<groupName>", … })
# 通知グループの一覧取得
client.get("/notification-groups")
# 通知グループの更新
client.put("/notification-groups/<notificationGroupId>", {"name": "<groupName>", … })
# 通知グループの削除
client.delete("/notification-groups/<notificationGroupId>")
```

### alert

```python
# アラートの一覧
client.get("/alerts")
# アラートの取得
client.get("/alerts/<alertId>")
# アラートを閉じる
client.post("/alerts/<alertId>/close", {"reason": "<text>"})
```

### alert group

```python
# アラートグループ設定の一覧
client.get("/alert-group-settings")
# アラートグループ設定の作成
client.post("/alert-group-settings", {"name": "<alertGroupName>", … })
# アラートグループ設定の取得
client.get("/alert-group-settings/<alertGroupSettingId>")
# アラートグループ設定の更新
client.put("/alert-group-settings/<alertGroupSettingId>", {"name": "<groupName>", … })
# アラートグループ設定の削除
client.delete("/alert-group-settings/<alertGroupSettingId>")
```

### dashboard

```python
# ダッシュボードの作成
client.post("/dashboards", {"title": "<dashboardTitle>", … })
# ダッシュボードの取得
client.get("/dashboards/<dashboardId>")
# ダッシュボードの更新
client.put("/dashboards/<dashboardId>", {"title": "<dashboardTitle>", … })
# ダッシュボードの削除
client.delete("/dashboards/<dashboardId>")
# ダッシュボードの一覧
client.get("/dashboards")
```

### graph annotation

```python
# グラフアノテーションの作成
client.post("/graph-annotations", {"title": "<annotationTitle>", … })
# グラフアノテーションの取得
client.get("/graph-annotations", {"service": "<serviceName>", … })
# グラフアノテーションの更新
client.put("/graph-annotations/<annotationId>", {"title": "<annotationTitle>", … })
# グラフアノテーションの削除
client.delete("/graph-annotations/<annotationId>")
```

### user

```python
# オーガニゼーションメンバーに所属するユーザーの一覧
client.get("/users")
# オーガニゼーションメンバーに所属するユーザーの削除
client.delete("/users/<userId>")
```

### invitation

```python
# 招待の一覧
client.get("/invitations")
# 招待の作成
client.post("/invitations", {"email": "<emailAddress>", … })
# 招待の取り消し
client.post("/invitations/revoke", {"email": "<emailAddress>", … })
```

### org

```python
# オーガニゼーションの情報を取得
client.get("/org")
```

### aws integration

```python
# AWSインテグレーション設定の一覧
client.get("/aws-integrations")
# AWSインテグレーション設定の取得
client.get("/aws-integrations/<awsIntegrationId>")
# AWSインテグレーション設定の登録
client.post("/aws-integrations", {"name": "<awsIntegrationName>, … "})
# AWSインテグレーション設定の更新
client.put("/aws-integrations/<awsIntegrationId>", {"name": "<awsIntegrationName>", … })
# AWSインテグレーション設定の削除
client.delete("aws-integrations/<awsIntegrationId>")
# AWSインテグレーション外部IDの生成
client.post("/aws-integrations-external-id")
# AWSインテグレーションの除外可能なメトリック名一覧
client.get("/aws-integrations-excludable-metrics")
```
