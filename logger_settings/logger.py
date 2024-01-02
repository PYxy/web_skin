import logging.config
import os

from web_skin.settings import DEBUG

cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个

debug_flag = DEBUG


# 给过滤器使用的判断
class RequireDebugTrue(logging.Filter):
    # 实现filter方法
    def filter(self, record):
        return debug_flag


logging_config = {
    # 必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1
    'version': 1,
    # 是否禁用现有的记录器
    'disable_existing_loggers': False,

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': RequireDebugTrue,  # 在开发环境，我设置DEBUG为True；在客户端，我设置DEBUG为False。从而控制是否需要使用某些处理器。
        }
    },

    # 日志格式集合
    'formatters': {

        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(funcName)s]- '
                      '%(levelname)s-%(message)s'},

    },

    # 处理器集合
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'all.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小
            'backupCount': 10,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error.log'),
            'maxBytes': 1024 * 1024 * 10,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'encoding': 'utf-8',  # 设置默认编码
        },

        'User': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 用这'logging.StreamHandler' 日志信息才会输出到console
            # 'filename': os.path.join(log_path, 'mongo_resist.log'),
            # 'maxBytes': 1024 * 1024 * 10,
            # 'backupCount': 5,
            'formatter': 'standard',
            # 'encoding': 'utf-8',  # 设置默认编码
        },
        'console': {
            'class': 'logging.StreamHandler',  # 用这'logging.StreamHandler' 日志信息才会输出到console
        },

    },

    # 日志管理器集合
    'loggers': {
        'root': {
            'handlers': ["default", "error", ],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器
        },
        'user': {
            'handlers': ['User', "default", "error"],
            'level': 'DEBUG',
            'propagate': True,  # 是否传递给父记录器,
        },
        'console': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger('root')

# 只输出到控制台
console = logging.getLogger("console")