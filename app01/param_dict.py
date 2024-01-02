from pkg.base_class.base_class import CheckDict, ParamLegitimacy

param = {
    # create_get 就是 url 中的请求路径 /user/create 中的create get
    "create_get": CheckDict(
        {
            # id 是参数   ["1", "2"] id 只能在 1 2 之间选
            "id": {"function": ParamLegitimacy.c_limit, "param": [["1", "2"], ]},
            # name 也是参数 .{1,3} 表示 1到3个字符
            "name": {"function": ParamLegitimacy.c_pattern, "param": [".{1,3}", ]},
            "age": {"function": ParamLegitimacy.lazy_to_do, "param": []},  # 这样写表示不校验 但是参数还是得传,不然默认为 "" 空字符串
        }
    ),
    # create_post 就是 url 中的请求路径 /user/create 中的create post
    "create_post": CheckDict(
        {
            "task_id": {"function": ParamLegitimacy.c_pattern, "param": ["\d{1,}", ]}
        }
    ),

    "create_put": CheckDict(
        {
            # id 是参数   ["1", "2"] id 只能在 1 2 之间选
            "id": {"function": ParamLegitimacy.c_limit, "param": [["1", "2"], ]},
            # name 也是参数 .{1,3} 表示 1到3个字符
            "name": {"function": ParamLegitimacy.c_pattern, "param": [".{1,3}", ]}
        }
    ),

    "create_delete": CheckDict(
        {
            # id 是参数   ["1", "2"] id 只能在 1 2 之间选
            "id": {"function": ParamLegitimacy.c_limit, "param": [["1", "2"], ]},
            # name 也是参数 .{1,3} 表示 1到3个字符
            "name": {"function": ParamLegitimacy.c_pattern, "param": [".{1,3}", ]}
        }
    ),

}
