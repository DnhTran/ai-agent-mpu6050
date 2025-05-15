# Makefile cho AI Agent

.PHONY: run setup clean logs

PYTHON = venv/bin/python

run:
	@echo "🚀 Đang chạy AI Agent..."
	@$(PYTHON) main.py

setup:
	@echo "🔧 Thiết lập môi trường ảo và cài đặt thư viện..."
	@python3 -m venv venv
	@venv/bin/pip install -r requirements.txt

logs:
	@echo "📄 Hiển thị log các trạng thái:"
	@cat logs/agent_history.csv || echo "⚠️ Không có log."

clean:
	@echo "🧹 Xóa logs và môi trường..."
	@rm -rf logs agent_history.csv venv __pycache__
