#!/usr/bin/env bash
# exit on error
set -o errexit

# 本番環境のライブラリをインポート
pip install -r requirements.txt


# プロジェクト内の静的ファイルを一箇所に集める(本番環境に必要)
# settings.pyの SECRET_ROOTの場所に格納
python manage.py collectstatic --noinput
# 本番環境のDBにmigrationファイルの設定を反映
python manage.py migrate
# 本番環境用の管理ユーザーを作成
# 2回目以降のデプロイでは不要のため、コメントアウト
# python manage.py createsuperuser --username admin --email admin@test.com --noinput