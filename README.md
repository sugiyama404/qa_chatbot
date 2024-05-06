# 自然言語処理(Sentence-BERT)を使った高信頼性AIチャットボット

<p align="center">
  <img src="sources/qanda.gif" alt="animated" width="400">
</p>

![Git](https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white)
![gitignore](https://img.shields.io/badge/gitignore%20io-204ECF?logo=gitignoredotio&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?logo=terraform&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?logo=javascript&logoColor=F7DF1E)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?logo=node.js&logoColor=white)
![Nuxtjs](https://img.shields.io/badge/Nuxt-3.11.2-blue.svg?logo=nuxtdotjs&logoColor=#00DC82)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python&logoColor=blue)](https://www.python.org/)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-blue.svg?logo=fastapi)
![Pandas](https://img.shields.io/badge/pandas-2.2.2-blue.svg?logo=pandas&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.2.2-blue.svg?logo=PyTorch&logoColor=white)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3-blue.svg)](https://docs.docker.com/compose/)
[![Pytest](https://img.shields.io/badge/pytest-8.1.1-blue.svg)](https://pytest.org/)
[![jQuery](https://img.shields.io/badge/jQuery-3.7.1-blue.svg?logo=jquery&logoColor=white)](https://jquery.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
![Commit Msg](https://img.shields.io/badge/Commit%20message-Eg-brightgreen.svg)
![Code Cmnt](https://img.shields.io/badge/code%20comment-Ja-brightgreen.svg)


従来のチャットボットでは誤回答のリスクがありましたが、今回開発したAIチャットボットは、最初から質問と答えを用意することで、高信頼性を実現しました。これは、Sentence BERTを使い、質問と回答に対して類似文章検索を行っています。

# インフラ構成

<p align="center">
  <img src="sources/aws.png" alt="animated" width="400">
</p>

+ Amazon S3 (Simple Storage Service): オブジェクトストレージサービス。静的コンテンツ、アプリケーションデータ、バックアップデータなどを保存するために使用します。
+ Amazon API Gateway: RESTful API を構築、デプロイ、管理するためのサービス。API クライアントからのリクエストを処理し、バックエンドサービスにルーティングします。
+ Amazon CloudWatch: モニタリングおよびログ収集サービス。インフラ、アプリケーション、およびログを監視するために使用します。
+ Amazon CloudFront: コンテンツ配信ネットワーク (CDN)。静的コンテンツを世界中のユーザーに低遅延で配信するために使用します。
+ Amazon Elastic Load Balancing (ELB): トラフィックを複数のロードバランサーに分散させるサービス。アプリケーションの可用性とスケーラビリティを向上させるために使用します。
+ Amazon Fargate: コンテナーサービス。サーバーをプロビジョニングおよび管理することなく、コンテナーをデプロイおよび実行するために使用します。
+ Amazon Elastic Container Registry (ECR): コンテナーイメージを保存および管理するためのプライベートレジストリサービス。

# システム構成
+ FastAPI: Python製の高性能Webフレームワーク。
+ Nuxt.js: Vue.js製のユニバーサルアプリケーションフレームワーク。

# 起動とデプロイ方法
1. 以下のコードを実行してWebサーバーをビルドします。
```
bin/webserver_build
```

2. 以下のコードを実行してインフラを構築し、APIサーバーをデプロイします。
```
bin/terraform_apply
```

3. webserver/app/.output/publicのアップロード
    1. ローカル環境で webserver/app/.output/publicディレクトリを開きます。
    2. S3 バケットに webserver/app/.output/publicディレクトリ配下のファイルをアップロードします。

4. CloudFrontからドメイン名を取得
    1. AWS マネジメントコンソールで Amazon CloudFrontサービスに移動します。
    2. ディストリビューション一覧から、目的のディストリビューションを選択します。
    3. ディストリビューション画面が表示されたら、 ディストリビューションドメイン名をコピーします。
5. URLにアクセス
    1. ブラウザを開き、先ほどコピーしたURLにアクセスします。

# 停止
以下のコードを実行すると停止できます。
```
bin/terraform_destroy
```

# テスト項目
+ GETメソッドによるルートエンドポイントの正常処理検証テスト
+ POSTメソッドによる正常処理テスト (クエリパラメータあり)
+ クエリに不正な値が渡された場合の挙動検証テストケース
+ クエリが省略された場合の挙動検証テストケース

# テスト結果

<p align="center">
  <img src="sources/test.png" alt="animated">
</p>

















