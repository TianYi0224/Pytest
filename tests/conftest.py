# 可以在这里定义项目级别的夹具和配置
import pytest
import logging

# 示例：设置全局测试超时时间为5秒
# @pytest.fixture(autouse=True)
# def set_timeout():
#     pytest.set_timeout(5)



# def pytest_configure(config):
#     # 创建日志目录
#     import os
#     log_dir = os.path.join(os.getcwd(), "logs")
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)
    
#     # 配置根日志记录器
#     root_logger = logging.getLogger()
#     root_logger.setLevel(logging.DEBUG)  # 捕获所有级别的日志
    
#     # 创建文件处理器
#     log_file = os.path.join(log_dir, "pytest1.log")
#     file_handler = logging.FileHandler(log_file, mode="w")
#     file_handler.setLevel(logging.DEBUG)
    
#     # 创建控制台处理器
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.DEBUG)  # 控制台也显示所有级别的日志
    
#     # 创建格式化器
#     formatter = logging.Formatter(
#         "%(asctime)s - %(levelname)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S"
#     )
    
#     # 添加格式化器到处理器
#     file_handler.setFormatter(formatter)                # 这里的格式如果在有pytest.ini配置的情况下，是不会生效的
#     console_handler.setFormatter(formatter)
    
#     # 添加处理器到根日志记录器
#     root_logger.addHandler(file_handler)
#     root_logger.addHandler(console_handler)
    
#     # 记录配置完成
#     root_logger.info("Pytest logging configured")