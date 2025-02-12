[
    {
        "name": "获取事件出口 IP",
        "detail": "飞书开放平台向应用配置的回调地址推送事件时，是通过特定的 IP 发送出去的，应用可以通过本接口获取所有相关的 IP 地址。",
        "bizTag": "event"
    },
    {
        "name": "获取用户信息",
        "detail": "通过 `user_access_token` 获取登录用户的信息。",
        "bizTag": "auth"
    },
    {
        "name": "批量获取脱敏的用户登录信息",
        "detail": "该接口用于查询用户的登录信息。",
        "bizTag": "passport"
    },
    {
        "name": "退出登录",
        "detail": "",
        "bizTag": "passport"
    },
    {
        "name": "自建应用获取 tenant_access_token",
        "detail": "企业自建应用通过此接口获取 tenant_access_token，调用接口获取企业资源时，需要使用 tenant_access_token 作为授权凭证。",
        "bizTag": "auth"
    },
    {
        "name": "自建应用获取 app_access_token",
        "detail": "企业自建应用通过此接口获取 app_access_token，调用接口获取应用资源时，需要使用 app_access_token 作为授权凭证。",
        "bizTag": "auth"
    },
    {
        "name": "重新获取 app_ticket",
        "detail": "飞书每隔 1 小时会给应用推送一次最新的 app_ticket，应用也可以主动调用此接口，触发飞书进行及时的重新推送。（该接口并不能直接获取app_ticket，而是触发事件推送）",
        "bizTag": "auth"
    },
    {
        "name": "商店应用获取 app_access_token",
        "detail": "应用商店应用通过此接口获取 app_access_token，调用接口获取应用资源时，需要使用 app_access_token 作为授权凭证。",
        "bizTag": "auth"
    },
    {
        "name": "商店应用获取 tenant_access_token",
        "detail": "应用商店应用通过此接口获取 tenant_access_token，调用接口获取企业资源时，需要使用 tenant_access_token 作为授权凭证。",
        "bizTag": "auth"
    },
    {
        "name": "获取通讯录授权范围",
        "detail": "该接口用于获取应用被授权可访问的通讯录范围，包括可访问的部门列表、用户列表和用户组列表。\n授权范围为全员时，返回的部门列表为该企业所有的一级部门；否则返回的部门为管理员在设置授权范围时勾选的部门（不包含勾选部门的子部门）。",
        "bizTag": "contact"
    },
    {
        "name": "创建用户",
        "detail": "使用该接口向通讯录创建一个用户，可以理解为员工入职。创建用户后只返回有数据权限的数据。具体的数据权限的与字段的对应关系请参照[应用权限](/ssl:ttdoc/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)。",
        "bizTag": "contact"
    },
    {
        "name": "修改用户部分信息",
        "detail": "该接口用于更新通讯录中用户的字段，未传递的参数不会更新。",
        "bizTag": "contact"
    },
    {
        "name": "更新用户 ID",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取单个用户信息",
        "detail": "该接口用于获取通讯录中单个用户的信息。",
        "bizTag": "contact"
    },
    {
        "name": "批量获取用户信息",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取部门直属用户列表",
        "detail": "基于部门ID获取部门直属用户列表。",
        "bizTag": "contact"
    },
    {
        "name": "通过手机号或邮箱获取用户 ID",
        "detail": "通过该接口，可使用手机号/邮箱获取用户的 ID 信息，具体获取支持的 ID 类型包括 open_id、user_id、union_id，可通过查询参数指定。",
        "bizTag": "contact"
    },
    {
        "name": "搜索用户",
        "detail": "以用户身份搜索其他用户的信息，无法搜索到外部企业或已离职的用户。",
        "bizTag": "contact"
    },
    {
        "name": "删除用户",
        "detail": "该接口用于从通讯录删除一个用户信息，可以理解为员工离职。",
        "bizTag": "contact"
    },
    {
        "name": "恢复已删除用户",
        "detail": "该接口用于恢复已删除用户（已离职的成员），仅自建应用可申请，应用商店应用无权调用接口。",
        "bizTag": "contact"
    },
    {
        "name": "创建用户组",
        "detail": "使用该接口创建用户组，请注意创建用户组时应用的通讯录权限范围需为“全部员工”，否则会创建失败，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "更新用户组",
        "detail": "使用该接口更新用户组信息，请注意更新用户组时应用的通讯录权限范围需为“全部员工”，否则会更新失败。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "查询指定用户组",
        "detail": "根据用户组 ID 查询某个用户组的基本信息，支持查询普通用户组和动态用户组。请确保应用的通讯录权限范围里包括该用户组或者是“全部员工”，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "查询用户组列表",
        "detail": "通过该接口可查询企业的用户组列表，可分别查询普通用户组或动态用户组。如果应用的通讯录权限范围是“全部员工”，则可获取企业全部用户组列表。如果应用的通讯录权限范围不是“全部员工”，则仅可获取通讯录权限范围内的用户组。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "查询用户所属用户组",
        "detail": "通过该接口可查询该用户所属的用户组列表，可分别查询普通用户组和动态用户组。如果应用的通讯录权限范围是“全部员工”，则可获取该员工所属的全部用户组列表。如果应用的通讯录权限范围不是“全部员工”，则仅可获取通讯录权限范围内该员工所属的用户组。[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "删除用户组",
        "detail": "通过该接口可删除企业中的用户组，请注意删除用户组时应用的通讯录权限范围需为“全部员工”，否则会删除失败，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "获取企业自定义用户字段",
        "detail": "获取企业自定义的用户字段配置信息",
        "bizTag": "contact"
    },
    {
        "name": "新增人员类型",
        "detail": "新增自定义人员类型。",
        "bizTag": "contact"
    },
    {
        "name": "更新人员类型",
        "detail": "更新自定义人员类型。",
        "bizTag": "contact"
    },
    {
        "name": "查询人员类型",
        "detail": "该接口用于获取员工的人员类型。",
        "bizTag": "contact"
    },
    {
        "name": "删除人员类型",
        "detail": "删除自定义人员类型。",
        "bizTag": "contact"
    },
    {
        "name": "创建部门",
        "detail": "该接口用于向通讯录中创建部门。",
        "bizTag": "contact"
    },
    {
        "name": "修改部门部分信息",
        "detail": "该接口用于更新通讯录中部门的信息。",
        "bizTag": "contact"
    },
    {
        "name": "更新部门所有信息",
        "detail": "该接口用于更新当前部门所有信息。",
        "bizTag": "contact"
    },
    {
        "name": "更新部门 ID",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "部门群转为普通群",
        "detail": "通过该接口将部门群转为普通群。",
        "bizTag": "contact"
    },
    {
        "name": "获取单个部门信息",
        "detail": "该接口用于向通讯录获取单个部门信息。",
        "bizTag": "contact"
    },
    {
        "name": "批量获取部门信息",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取子部门列表",
        "detail": "通过部门ID获取部门的子部门列表。",
        "bizTag": "contact"
    },
    {
        "name": "获取父部门信息",
        "detail": "该接口用来递归获取部门父部门的信息，并按照由子到父的顺序返回有权限的父部门信息列表。",
        "bizTag": "contact"
    },
    {
        "name": "搜索部门",
        "detail": "搜索部门，用户通过关键词查询可见的部门数据，部门可见性需要管理员在后台配置。",
        "bizTag": "contact"
    },
    {
        "name": "删除部门",
        "detail": "该接口用于从通讯录中删除部门。",
        "bizTag": "contact"
    },
    {
        "name": "创建单位",
        "detail": "该接口用于创建单位。注意：单位功能属于旗舰版付费功能，企业需开通对应版本才可以创建单位，不同版本请参考[飞书版本对比](https://www.feishu.cn/service)。",
        "bizTag": "contact"
    },
    {
        "name": "修改单位信息",
        "detail": "调用该接口，需要有更新单位的权限。注意：单位功能属于旗舰版付费功能，企业需开通对应版本才可以修改单位。",
        "bizTag": "contact"
    },
    {
        "name": "建立部门与单位的绑定关系",
        "detail": "通过该接口建立部门与单位的绑定关系。由于单位是旗舰版付费功能，企业需开通相关版本，否则会绑定失败，不同版本请参考[飞书版本对比](https://www.feishu.cn/service)。",
        "bizTag": "contact"
    },
    {
        "name": "解除部门与单位的绑定关系",
        "detail": "通过该接口解除部门与单位的绑定关系，需更新单位的权限，需对应部门的通讯录权限。由于单位是旗舰版付费功能，企业需开通相关功能，否则会解绑失败。",
        "bizTag": "contact"
    },
    {
        "name": "获取单位绑定的部门列表",
        "detail": "通过该接口获取单位绑定的部门列表，需具有获取单位的权限。",
        "bizTag": "contact"
    },
    {
        "name": "获取单位信息",
        "detail": "该接口用于获取单位信息。",
        "bizTag": "contact"
    },
    {
        "name": "获取单位列表",
        "detail": "通过该接口获取企业的单位列表，需获取单位的权限。",
        "bizTag": "contact"
    },
    {
        "name": "删除单位",
        "detail": "使用该接口删除单位，需要有更新单位的权限。注意：如果单位的单位类型被其它的业务使用，不允许删除。",
        "bizTag": "contact"
    },
    {
        "name": "添加用户组成员",
        "detail": "向用户组中添加成员(目前成员仅支持用户，未来会支持部门)，如果应用的通讯录权限范围是“全部员工”，则可将任何成员添加到任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员添加到通讯录权限范围的用户组中，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "批量添加用户组成员",
        "detail": "向普通用户组中批量添加成员(目前仅支持添加用户，暂不支持添加部门），如果应用的通讯录权限范围是“全部员工”，则可将任何成员添加到任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员添加到通讯录权限范围的用户组中，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "查询用户组成员列表",
        "detail": "通过该接口可查询某个用户组的成员列表（支持查询成员中的用户和部门）, 本接口支持普通用户组和动态用户组。如果应用的通讯录权限范围是“全部员工”，则可查询企业内任何用户组的成员列表。如果应用的通讯录权限范围不是“全部员工”，则仅可查询通讯录权限范围中的用户组的成员列表，[点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "移除用户组成员",
        "detail": "从用户组中移除成员 (目前成员仅支持用户，未来会支持部门)，如果应用的通讯录权限范围是“全部员工”，则可将任何成员移出任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员从通讯录权限范围的用户组中移除， [点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "批量移除用户组成员",
        "detail": "从普通用户组中批量移除成员 (目前仅支持移除用户，暂不支持移除部门）。如果应用的通讯录权限范围是“全部员工”，则可将任何成员移出任何用户组。如果应用的通讯录权限范围不是“全部员工”，则仅可将通讯录权限范围中的成员从通讯录权限范围的用户组中移除， [点击了解通讯录权限范围](/ssl:ttdoc/ukTMukTMukTM/uETNz4SM1MjLxUzM/v3/guides/scope_authority)。",
        "bizTag": "contact"
    },
    {
        "name": "创建角色",
        "detail": "通过”创建角色“接口可批量完成角色创建，新增角色同步展示至租户的管理后台-角色管理模块。",
        "bizTag": "contact"
    },
    {
        "name": "修改角色名称",
        "detail": "通过本接口可以修改角色名称",
        "bizTag": "contact"
    },
    {
        "name": "删除角色",
        "detail": "通过本接口可以删除某个角色",
        "bizTag": "contact"
    },
    {
        "name": "批量添加角色成员",
        "detail": "通过”批量添加角色成员“接口可批量添加成员，成员信息同步展示至租户的管理后台-角色管理模块。",
        "bizTag": "contact"
    },
    {
        "name": "批量设置角色成员管理范围",
        "detail": "通过该接口可设置本租户下角色成员的管理范围，以便在审批等场景中应用。",
        "bizTag": "contact"
    },
    {
        "name": "查询角色下某个成员的管理范围",
        "detail": "通过本接口可以查询某个成员的管理范围",
        "bizTag": "contact"
    },
    {
        "name": "查询角色下的所有成员信息",
        "detail": "通过本接口可以查询角色ID下的成员信息（含成员ID及其管理范围）",
        "bizTag": "contact"
    },
    {
        "name": "删除角色下的成员",
        "detail": "通过本接口可以删除角色下的某个/些成员",
        "bizTag": "contact"
    },
    {
        "name": "创建职级",
        "detail": "该接口可以创建职级。",
        "bizTag": "contact"
    },
    {
        "name": "更新职级",
        "detail": "该接口用于更新职级信息。",
        "bizTag": "contact"
    },
    {
        "name": "获取单个职级信息",
        "detail": "该接口可以获取单个职级的信息。",
        "bizTag": "contact"
    },
    {
        "name": "获取租户职级列表",
        "detail": "该接口可以获取租户职级列表。",
        "bizTag": "contact"
    },
    {
        "name": "删除职级",
        "detail": "该接口用于删除职级。",
        "bizTag": "contact"
    },
    {
        "name": "创建序列",
        "detail": "该接口用于创建租户内的序列信息。",
        "bizTag": "contact"
    },
    {
        "name": "更新序列",
        "detail": "该接口用于更新租户序列的信息。",
        "bizTag": "contact"
    },
    {
        "name": "获取单个序列信息",
        "detail": "该接口用于获取单个序列信息。",
        "bizTag": "contact"
    },
    {
        "name": "获取租户序列列表",
        "detail": "该接口用于获取租户序列列表。",
        "bizTag": "contact"
    },
    {
        "name": "删除序列",
        "detail": "该接口用于删除租户内的序列。",
        "bizTag": "contact"
    },
    {
        "name": "获取单个职务信息",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取租户职务列表",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取单个工作城市信息",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "获取租户工作城市列表",
        "detail": "",
        "bizTag": "contact"
    },
    {
        "name": "发送消息",
        "detail": "给指定用户或者会话发送消息，支持文本、富文本、可交互的[消息卡片](/ssl:ttdoc/ukTMukTMukTM/uczM3QjL3MzN04yNzcDN)、群名片、个人名片、图片、视频、音频、文件、表情包。",
        "bizTag": "im"
    },
    {
        "name": "回复消息",
        "detail": "回复指定消息，支持文本、富文本、卡片、群名片、个人名片、图片、视频、文件等多种消息类型。",
        "bizTag": "im"
    },
    {
        "name": "编辑消息",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "转发消息",
        "detail": "向一个用户或群聊转发一条指定消息。",
        "bizTag": "im"
    },
    {
        "name": "合并转发消息",
        "detail": "将来自同一个群聊中的多条消息合并转发给指定用户或群聊。",
        "bizTag": "im"
    },
    {
        "name": "转发话题",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "撤回消息",
        "detail": "机器人撤回机器人自己发送的消息或群主撤回群内消息。",
        "bizTag": "im"
    },
    {
        "name": "添加跟随气泡",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "查询消息已读信息",
        "detail": "查询消息的已读信息。",
        "bizTag": "im"
    },
    {
        "name": "获取会话历史消息",
        "detail": "获取会话（包括单聊、群组）的历史消息（聊天记录）。",
        "bizTag": "im"
    },
    {
        "name": "获取消息中的资源文件",
        "detail": "获取消息中的资源文件，包括音频，视频，图片和文件，**暂不支持表情包资源下载**。当前仅支持 100M 以内的资源文件的下载。",
        "bizTag": "im"
    },
    {
        "name": "获取指定消息的内容",
        "detail": "通过 message_id 查询消息内容。",
        "bizTag": "im"
    },
    {
        "name": "批量发送消息",
        "detail": "给多个用户或者多个部门发送消息。",
        "bizTag": "im"
    },
    {
        "name": "批量撤回消息",
        "detail": "批量撤回通过[批量发送消息](/ssl:ttdoc/ukTMukTMukTM/ucDO1EjL3gTNx4yN4UTM)接口发送的消息。",
        "bizTag": "im"
    },
    {
        "name": "查询批量消息推送和阅读人数",
        "detail": "批量发送消息后，可以通过该接口查询批量消息推送的总人数和阅读人数。",
        "bizTag": "im"
    },
    {
        "name": "查询批量消息整体进度",
        "detail": "该接口在[查询批量消息推送和阅读人数](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/im-v1/batch_message/read_user)查询结果的基础上，增加了批量请求中有效的userid数量以及消息撤回进度数据。",
        "bizTag": "im"
    },
    {
        "name": "上传图片",
        "detail": "上传图片接口，支持上传 JPEG、PNG、WEBP、GIF、TIFF、BMP、ICO格式图片。",
        "bizTag": "im"
    },
    {
        "name": "下载图片",
        "detail": "下载图片资源，只能下载当前应用所上传且图片类型为message的图片。",
        "bizTag": "im"
    },
    {
        "name": "上传文件",
        "detail": "上传文件，可以上传视频，音频和常见的文件类型。",
        "bizTag": "im"
    },
    {
        "name": "下载文件",
        "detail": "下载文件接口，只能下载应用自己上传的文件。",
        "bizTag": "im"
    },
    {
        "name": "发送应用内加急",
        "detail": "对指定消息进行应用内加急。",
        "bizTag": "im"
    },
    {
        "name": "发送短信加急",
        "detail": "对指定消息进行应用内加急与短信加急。",
        "bizTag": "im"
    },
    {
        "name": "发送电话加急",
        "detail": "对指定消息进行应用内加急与电话加急。",
        "bizTag": "im"
    },
    {
        "name": "添加消息表情回复",
        "detail": "给指定消息添加指定类型的表情回复（reaction即表情回复，本文档统一用“reaction”代称）。",
        "bizTag": "im"
    },
    {
        "name": "获取消息表情回复",
        "detail": "获取指定消息的特定类型表情回复列表（reaction即表情回复，本文档统一用“reaction”代称）。",
        "bizTag": "im"
    },
    {
        "name": "删除消息表情回复",
        "detail": "删除指定消息的表情回复（reaction即表情回复，本文档统一用“reaction”代称）。",
        "bizTag": "im"
    },
    {
        "name": "Pin 消息",
        "detail": "Pin 一条指定的消息。",
        "bizTag": "im"
    },
    {
        "name": "移除 Pin 消息",
        "detail": "移除一条指定消息的 Pin。",
        "bizTag": "im"
    },
    {
        "name": "获取群内 Pin 消息",
        "detail": "获取所在群内指定时间范围内的所有 Pin 消息。",
        "bizTag": "im"
    },
    {
        "name": "更新应用发送的消息卡片",
        "detail": "更新应用已发送的消息卡片内容。",
        "bizTag": "im"
    },
    {
        "name": "延时更新消息卡片",
        "detail": "用于用户交互完成后延后更新消息卡片。",
        "bizTag": "im"
    },
    {
        "name": "发送仅特定人可见的消息卡片",
        "detail": "用于机器人在群会话中发送仅指定用户可见的消息卡片。",
        "bizTag": "im"
    },
    {
        "name": "删除仅特定人可见的消息卡片",
        "detail": "在群会话中删除指定用户可见的临时消息卡片临时卡片消息可以通过该接口进行显式删除，临时卡片消息删除后将不会在该设备上留下任何痕迹。",
        "bizTag": "im"
    },
    {
        "name": "更新 URL 预览",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "创建群",
        "detail": "创建群并设置群头像、群名、群描述等。",
        "bizTag": "im"
    },
    {
        "name": "解散群",
        "detail": "解散群组。",
        "bizTag": "im"
    },
    {
        "name": "更新群信息",
        "detail": "更新群头像、群名称、群描述、群配置、转让群主等。",
        "bizTag": "im"
    },
    {
        "name": "更新群发言权限",
        "detail": "更新群组的发言权限设置，可设置为全员可发言、仅管理员可发言  或 指定用户可发言。",
        "bizTag": "im"
    },
    {
        "name": "获取群信息",
        "detail": "获取群名称、群描述、群头像、群主 ID 等群基本信息。",
        "bizTag": "im"
    },
    {
        "name": "更新群置顶",
        "detail": "更新会话中的群置顶信息，可以将群中的某一条消息，或者群公告置顶显示。",
        "bizTag": "im"
    },
    {
        "name": "撤销群置顶",
        "detail": "撤销会话中的置顶。",
        "bizTag": "im"
    },
    {
        "name": "获取用户或机器人所在的群列表",
        "detail": "获取用户或者机器人所在群列表。",
        "bizTag": "im"
    },
    {
        "name": "搜索对用户或机器人可见的群列表",
        "detail": "搜索对用户或机器人可见的群列表，包括：用户或机器人所在的群、对用户或机器人公开的群。\n搜索可获得的群信息包括：群ID（chat_id）、群名称、群描述等。",
        "bizTag": "im"
    },
    {
        "name": "获取群成员发言权限",
        "detail": "获取群发言模式、可发言用户名单等。",
        "bizTag": "im"
    },
    {
        "name": "获取群分享链接",
        "detail": "获取指定群的分享链接。",
        "bizTag": "im"
    },
    {
        "name": "指定群管理员",
        "detail": "将用户或机器人指定为群管理员。",
        "bizTag": "im"
    },
    {
        "name": "删除群管理员",
        "detail": "删除指定的群管理员（用户或机器人）。",
        "bizTag": "im"
    },
    {
        "name": "将用户或机器人拉入群聊",
        "detail": "将用户或机器人拉入群聊。",
        "bizTag": "im"
    },
    {
        "name": "用户或机器人主动加入群聊",
        "detail": "用户或机器人主动加入群聊。",
        "bizTag": "im"
    },
    {
        "name": "将用户或机器人移出群聊",
        "detail": "将用户或机器人移出群聊。",
        "bizTag": "im"
    },
    {
        "name": "获取群成员列表",
        "detail": "获取用户/机器人所在群的群成员列表。",
        "bizTag": "im"
    },
    {
        "name": "判断用户或机器人是否在群里",
        "detail": "根据使用的access_token判断对应的用户或者机器人是否在群里。",
        "bizTag": "im"
    },
    {
        "name": "获取群公告基本信息",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "获取群公告所有块",
        "detail": "获取群公告所有块的富文本内容并分页返回。\n",
        "bizTag": "ccm"
    },
    {
        "name": "在群公告中创建块",
        "detail": "在指定块的子块列表中，新创建一批子块，并放置到指定位置。如果操作成功，接口将返回新创建子块的富文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "批量更新群公告块的内容",
        "detail": "批量更新块的富文本内容。\n",
        "bizTag": "ccm"
    },
    {
        "name": "获取群公告块的内容",
        "detail": "获取指定块的富文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "获取所有子块",
        "detail": "获取群公告中指定块的所有子块的富文本内容并分页返回。\n",
        "bizTag": "ccm"
    },
    {
        "name": "删除群公告中的块",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "更新群公告信息",
        "detail": "更新会话中的群公告信息，更新公告信息的格式和更新[云文档](https://open.feishu.cn/document/ukTMukTMukTM/uAzM5YjLwMTO24CMzkjN)格式相同。",
        "bizTag": "im"
    },
    {
        "name": "获取群公告信息",
        "detail": "获取会话中的群公告信息，公告信息格式与[云文档](https://open.feishu.cn/document/ukTMukTMukTM/uAzM5YjLwMTO24CMzkjN)格式相同。",
        "bizTag": "im"
    },
    {
        "name": "添加会话标签页",
        "detail": "添加自定义会话标签页。",
        "bizTag": "im"
    },
    {
        "name": "删除会话标签页",
        "detail": "删除会话标签页。",
        "bizTag": "im"
    },
    {
        "name": "更新会话标签页",
        "detail": "更新会话标签页。",
        "bizTag": "im"
    },
    {
        "name": "会话标签页排序",
        "detail": "会话标签页排序。",
        "bizTag": "im"
    },
    {
        "name": "拉取会话标签页",
        "detail": "拉取会话标签页。",
        "bizTag": "im"
    },
    {
        "name": "添加群菜单",
        "detail": "该接口用于向群组中添加群菜单。",
        "bizTag": "im"
    },
    {
        "name": "删除群菜单",
        "detail": "该接口用于删除群内已经添加的群菜单。",
        "bizTag": "im"
    },
    {
        "name": "修改群菜单元信息",
        "detail": "修改某个一级菜单或者二级菜单的元信息，包括群菜单的图标、名称、国际化名称和跳转链接。",
        "bizTag": "im"
    },
    {
        "name": "排序群菜单",
        "detail": "给一个群内的一级菜单排序。",
        "bizTag": "im"
    },
    {
        "name": "获取群菜单",
        "detail": "通过群 ID 获取群内菜单。",
        "bizTag": "im"
    },
    {
        "name": "创建应用消息流卡片",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "更新应用消息流卡片",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "删除应用消息流卡片",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "机器人单聊即时提醒",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "更新消息流卡片按钮",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "即时提醒",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "查询实体与标签的绑定关系",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "创建标签",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "修改标签",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "绑定标签到群",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "解绑标签与群",
        "detail": "",
        "bizTag": "im"
    },
    {
        "name": "创建卡片实体",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "更新卡片配置",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "批量更新卡片实体",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "全量更新卡片实体",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "转换 ID",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "新增组件",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "更新组件",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "更新组件属性",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "流式更新文本",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "删除组件",
        "detail": "",
        "bizTag": "cardkit"
    },
    {
        "name": "获取我的空间（root folder）元数据",
        "detail": "获取 \"我的空间\" 的元信息。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件夹中的文件清单",
        "detail": "获取用户云空间中指定文件夹下的文件清单。清单类型包括文件、各种在线文档（文档、电子表格、多维表格、思维笔记）、文件夹和快捷方式。该接口支持分页，但是不会递归的获取子文件夹的清单。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件夹元数据",
        "detail": "根据 folderToken 获取该文件夹的元信息。",
        "bizTag": "ccm"
    },
    {
        "name": "新建文件夹",
        "detail": "在用户云空间的指定文件夹中创建一个新的空文件夹。",
        "bizTag": "ccm"
    },
    {
        "name": "查询异步任务状态",
        "detail": "查询删除文件夹等异步任务的状态信息。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件元数据",
        "detail": "该接口用于根据 token 获取各类文件的元数据",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件统计信息",
        "detail": "此接口用于获取文件统计信息，包括文档阅读人数、次数和点赞数。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件访问记录",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "复制文件",
        "detail": "将文件复制到用户云空间的其他文件夹中。不支持复制文件夹。\n\n如果目标文件夹是我的空间，则复制的文件会在「**我的空间**」的「**归我所有**」列表里。",
        "bizTag": "ccm"
    },
    {
        "name": "移动文件或文件夹",
        "detail": "将文件或者文件夹移动到用户云空间的其他位置。",
        "bizTag": "ccm"
    },
    {
        "name": "删除文件或文件夹",
        "detail": "删除用户在云空间内的文件或者文件夹。文件或者文件夹被删除后，会进入用户回收站里。",
        "bizTag": "ccm"
    },
    {
        "name": "创建文件快捷方式",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "搜索云文档",
        "detail": "根据搜索条件进行文档搜索。",
        "bizTag": "ccm"
    },
    {
        "name": "上传文件",
        "detail": "向云空间指定目录下上传一个小文件。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传文件-预上传",
        "detail": "发送初始化请求获取上传事务ID和分块策略，目前是以4MB大小进行定长分片。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传文件-上传分片",
        "detail": "上传对应的文件块。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传文件-完成上传",
        "detail": "触发完成上传。",
        "bizTag": "ccm"
    },
    {
        "name": "下载文件",
        "detail": "下载云空间下的文件，不含飞书文档、电子表格以及多维表格等在线文档，支持指定文件 Range 进行下载。",
        "bizTag": "ccm"
    },
    {
        "name": "创建导入任务",
        "detail": "创建导入任务。支持导入为新版文档、电子表格、多维表格以及旧版文档。该接口为异步接口，需要通过[查询导入结果](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/get)接口获取导入结果，调用方式可参考[导入使用指南](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/import-user-guide)。",
        "bizTag": "ccm"
    },
    {
        "name": "查询导入任务结果",
        "detail": "根据创建导入任务返回的`ticket`轮询导入结果，调用方式可参考[导入使用指南](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/import_task/import-user-guide)。",
        "bizTag": "ccm"
    },
    {
        "name": "创建导出任务",
        "detail": "创建导出任务，将云文档导出为指定格式的本地文件，目前支持新版文档、电子表格、多维表格和旧版文档。该接口为异步接口，任务创建完成即刻返回，并不会阻塞等待到任务执行成功，因此需要结合[查询导出任务结果](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/export_task/get)接口获取导出结果。",
        "bizTag": "ccm"
    },
    {
        "name": "查询导出任务结果",
        "detail": "根据[创建导出任务](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/export_task/create)返回的`ticket`轮询导出任务的结果，通过本接口获取到导出产物的文件`token`之后，可调用[下载导出文件](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/export_task/download)接口将导出产物下载到本地。",
        "bizTag": "ccm"
    },
    {
        "name": "下载导出文件",
        "detail": "根据[查询导出任务结果](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/export_task/get)返回的导出产物`token`，下载导出产物文件到本地。",
        "bizTag": "ccm"
    },
    {
        "name": "上传素材",
        "detail": "将文件、图片、视频等素材文件上传到指定云文档中。素材文件在云空间中不会显示，只会显示在对应云文档中。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传素材-预上传",
        "detail": "发送初始化请求获取上传事务ID和分块策略，目前是以4MB大小进行定长分片。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传素材-上传分片",
        "detail": "上传对应的文件块。",
        "bizTag": "ccm"
    },
    {
        "name": "分片上传素材-完成上传",
        "detail": "触发完成上传。",
        "bizTag": "ccm"
    },
    {
        "name": "下载素材",
        "detail": "下载各种类型文档中的素材，比如电子表格中的图片，支持指定`range`进行分片下载。",
        "bizTag": "ccm"
    },
    {
        "name": "获取素材临时下载链接",
        "detail": "通过`file_tokens`获取素材临时下载链接，链接时效性是 24 小时，过期失效。",
        "bizTag": "ccm"
    },
    {
        "name": "创建文档版本",
        "detail": "创建文档版本。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文档版本列表",
        "detail": "获取文档所有版本。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文档版本信息",
        "detail": "获取文档版本。",
        "bizTag": "ccm"
    },
    {
        "name": "删除文档版本",
        "detail": "删除文档版本。",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档的点赞者列表",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "订阅云文档事件",
        "detail": "该接口仅支持**文档拥有者**订阅自己文档的通知事件，可订阅的文档类型为**旧版文档**、**新版文档**、**电子表格**和**多维表格**。在调用该接口之前请确保正确[配置事件回调网址和订阅事件类型](/ssl:ttdoc/ukTMukTMukTM/uUTNz4SN1MjL1UzM#2eb3504a)(暂不支持单独订阅文档维度的某类事件)，事件类型参考[事件列表](/ssl:ttdoc/ukTMukTMukTM/uYDNxYjL2QTM24iN0EjN/event-list)。",
        "bizTag": "ccm"
    },
    {
        "name": "查询云文档事件订阅状态",
        "detail": "该接口**仅支持文档拥有者**查询自己文档的订阅状态，可订阅的文档类型为**旧版文档**、**新版文档**、**电子表格**和**多维表格**。在调用该接口之前请确保正确[配置事件回调网址和订阅事件类型](/ssl:ttdoc/ukTMukTMukTM/uUTNz4SN1MjL1UzM#2eb3504a)，事件类型参考[事件列表](/ssl:ttdoc/ukTMukTMukTM/uYDNxYjL2QTM24iN0EjN/event-list)。",
        "bizTag": "ccm"
    },
    {
        "name": "取消云文档事件订阅",
        "detail": "该接口**仅支持文档拥有者**取消订阅自己文档的通知事件，可订阅的文档类型为**旧版文档**、**新版文档**、**电子表格**和**多维表格**。暂时无法指定取消的具体事件类型，事件类型以开发者后台为准。在调用该接口之前请确保正确[配置事件回调网址和订阅事件类型](/ssl:ttdoc/ukTMukTMukTM/uUTNz4SN1MjL1UzM#2eb3504a)，事件类型参考[事件列表](/ssl:ttdoc/ukTMukTMukTM/uYDNxYjL2QTM24iN0EjN/event-list)。",
        "bizTag": "ccm"
    },
    {
        "name": "获取知识空间列表",
        "detail": "此接口用于获取有权限访问的知识空间列表。\n\n此接口为分页接口。由于权限过滤，可能返回列表为空，但分页标记（has_more）为true，可以继续分页请求。\n\n对于知识空间各项属性描述请参阅[获取知识空间信息](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get)",
        "bizTag": "ccm"
    },
    {
        "name": "获取知识空间信息",
        "detail": "此接口用于根据知识空间ID来查询知识空间的信息。\n\n空间类型（type）：\n- 个人空间：归个人管理。一人仅可拥有一个个人空间，无法添加其他管理员。\n- 团队空间：归团队（多人)管理，可添加多个管理员。\n\n空间可见性（visibility）：\n- 公开空间：租户所有用户可见，默认为成员权限。无法额外添加成员，但可以添加管理员。\n- 私有空间：仅对知识空间管理员、成员可见，需要手动添加管理员、成员。",
        "bizTag": "ccm"
    },
    {
        "name": "创建知识空间",
        "detail": "此接口用于创建知识空间",
        "bizTag": "ccm"
    },
    {
        "name": "获取知识空间成员列表",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "添加知识空间成员",
        "detail": "添加知识空间成员或管理员。",
        "bizTag": "ccm"
    },
    {
        "name": "删除知识空间成员",
        "detail": "此接口用于删除知识空间成员或管理员。",
        "bizTag": "ccm"
    },
    {
        "name": "更新知识空间设置",
        "detail": "根据space_id更新知识空间公共设置",
        "bizTag": "ccm"
    },
    {
        "name": "创建知识空间节点",
        "detail": "此接口用于在知识节点里创建[节点](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-overview)到指定位置。",
        "bizTag": "ccm"
    },
    {
        "name": "获取知识空间节点信息",
        "detail": "获取知识空间节点信息",
        "bizTag": "ccm"
    },
    {
        "name": "获取知识空间子节点列表",
        "detail": "此接口用于分页获取Wiki节点的子节点列表。\n\n此接口为分页接口。由于权限过滤，可能返回列表为空，但分页标记（has_more）为true，可以继续分页请求。",
        "bizTag": "ccm"
    },
    {
        "name": "移动知识空间节点",
        "detail": "此方法用于在Wiki内移动节点，支持跨知识空间移动。如果有子节点，会携带子节点一起移动。",
        "bizTag": "ccm"
    },
    {
        "name": "更新知识空间节点标题",
        "detail": "此接口用于更新节点标题",
        "bizTag": "ccm"
    },
    {
        "name": "创建知识空间节点副本",
        "detail": "此接口用于在知识空间创建节点副本到指定位置。",
        "bizTag": "ccm"
    },
    {
        "name": "移动云空间文档至知识空间",
        "detail": "该接口允许移动云空间文档至知识空间，并挂载在指定位置",
        "bizTag": "ccm"
    },
    {
        "name": "获取任务结果",
        "detail": "该方法用于获取wiki异步任务的结果",
        "bizTag": "ccm"
    },
    {
        "name": "搜索 Wiki",
        "detail": "搜索 Wiki，用户通过关键词查询 Wiki，只能查找自己可见的 wiki。",
        "bizTag": "ccm"
    },
    {
        "name": "创建文档",
        "detail": "创建新版文档，文档标题和目录可选。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文档基本信息",
        "detail": "获取文档最新版本号、标题等",
        "bizTag": "ccm"
    },
    {
        "name": "获取文档纯文本内容",
        "detail": "获取文档的纯文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文档所有块",
        "detail": "获取文档所有块的富文本内容并分页返回。",
        "bizTag": "ccm"
    },
    {
        "name": "创建块",
        "detail": "在指定块的子块列表中，新创建一批子块，并放置到指定位置。如果操作成功，接口将返回新创建子块的富文本内容。调用该接口前，你可参考[文档概述-基本概念](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview)了解块的父子关系规则。",
        "bizTag": "ccm"
    },
    {
        "name": "创建嵌套块",
        "detail": "在指定块的子块列表中，新创建一批有父子关系的子块，并放置到指定位置。如果操作成功，接口将返回新创建子块的富文本内容。调用该接口前，你可参考[文档概述-基本概念](/ssl:ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/document-docx/docx-overview)了解块的父子关系规则。当创建的子块中含有 GridColumn、TableCell、Callout 时其中至少需要包含一个子块 ，即内容为空时也需要填入一个空 Text Block 作为子块。",
        "bizTag": "ccm"
    },
    {
        "name": "更新块的内容",
        "detail": "更新指定块的内容。如果操作成功，接口将返回更新后的块的富文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "获取块的内容",
        "detail": "获取指定块的富文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "批量更新块的内容",
        "detail": "批量更新块的富文本内容。",
        "bizTag": "ccm"
    },
    {
        "name": "获取所有子块",
        "detail": "获取文档中指定块的所有子块的富文本内容并分页返回。文档版本号可选。",
        "bizTag": "ccm"
    },
    {
        "name": "删除块",
        "detail": "指定需要操作的块，删除其指定范围的子块。如果操作成功，接口将返回应用删除操作后的文档版本号。",
        "bizTag": "ccm"
    },
    {
        "name": "创建电子表格",
        "detail": "在指定目录下创建表格",
        "bizTag": "ccm"
    },
    {
        "name": "修改电子表格属性",
        "detail": "该接口用于修改电子表格的属性",
        "bizTag": "ccm"
    },
    {
        "name": "获取电子表格信息",
        "detail": "该接口用于获取电子表格的基础信息。",
        "bizTag": "ccm"
    },
    {
        "name": "操作工作表",
        "detail": "根据 spreadsheetToken 更新工作表属性。",
        "bizTag": "ccm"
    },
    {
        "name": "更新工作表属性",
        "detail": "根据 spreadsheetToken 更新工作表属性。",
        "bizTag": "ccm"
    },
    {
        "name": "获取工作表",
        "detail": "该接口用于获取电子表格下所有工作表及其属性。",
        "bizTag": "ccm"
    },
    {
        "name": "查询工作表",
        "detail": "该接口用于通过工作表ID查询工作表属性信息。",
        "bizTag": "ccm"
    },
    {
        "name": "增加行列",
        "detail": "根据 spreadsheetToken 和长度，在末尾增加空行/列；单次操作不超过5000行或列。",
        "bizTag": "ccm"
    },
    {
        "name": "插入行列",
        "detail": "根据 spreadsheetToken 和维度信息 插入空行/列。如 startIndex=3， endIndex=7，则从第 4 行开始开始插入行列，一直到第 7 行，共插入 4 行；单次操作不超过5000行或列。",
        "bizTag": "ccm"
    },
    {
        "name": "更新行列",
        "detail": "根据 spreadsheetToken 和维度信息更新隐藏行列、单元格大小；单次操作不超过5000行或列。",
        "bizTag": "ccm"
    },
    {
        "name": "移动行列",
        "detail": "该接口用于移动行列，行列被移动到目标位置后，原本在目标位置的行列会对应右移或下移。",
        "bizTag": "ccm"
    },
    {
        "name": "删除行列",
        "detail": "该接口用于根据 spreadsheetToken 和维度信息删除行/列 。单次删除最大5000行/列。",
        "bizTag": "ccm"
    },
    {
        "name": "合并单元格",
        "detail": "根据 spreadsheetToken 和维度信息合并单元格；单次操作不超过5000行，100列。",
        "bizTag": "ccm"
    },
    {
        "name": "拆分单元格",
        "detail": "根据 spreadsheetToken 和维度信息拆分单元格；单次操作不超过5000行，100列。",
        "bizTag": "ccm"
    },
    {
        "name": "查找单元格",
        "detail": "在指定范围内查找符合查找条件的单元格。",
        "bizTag": "ccm"
    },
    {
        "name": "替换单元格",
        "detail": "按照指定的条件查找子表的某个范围内的数据符合条件的单元格并替换值，返回替换成功的单元格位置。一次请求最多允许替换5000个单元格，如果超过请将range缩小范围再操作。请求体中的 range、find、replaccement 字段必填。",
        "bizTag": "ccm"
    },
    {
        "name": "设置单元格样式 ",
        "detail": "根据 spreadsheetToken 、range 和样式信息更新单元格样式；单次写入不超过5000行，100列。",
        "bizTag": "ccm"
    },
    {
        "name": "批量设置单元格样式 ",
        "detail": "根据 spreadsheetToken 、range和样式信息 批量更新单元格样式；单次写入不超过5000行，100列。",
        "bizTag": "ccm"
    },
    {
        "name": "插入数据",
        "detail": "根据 spreadsheetToken 和 range 向范围之前增加相应数据的行和相应的数据，相当于数组的插入操作；单次写入不超过5000行，100列，每个格子不超过5万字符。",
        "bizTag": "ccm"
    },
    {
        "name": "追加数据",
        "detail": "根据 spreadsheetToken 和 range 遇到空行则进行覆盖追加或新增行追加数据。 空行：默认该行第一个格子是空，则认为是空行；单次写入不超过5000行，100列，每个格子不超过5万字符。",
        "bizTag": "ccm"
    },
    {
        "name": "写入图片",
        "detail": "根据 spreadsheetToken 和 range 向单个格子写入图片。",
        "bizTag": "ccm"
    },
    {
        "name": "读取单个范围",
        "detail": "根据 spreadsheetToken 和 range 读取表格单个范围的值，返回数据限制为10M。",
        "bizTag": "ccm"
    },
    {
        "name": "读取多个范围",
        "detail": "根据 spreadsheetToken 和 ranges 读取表格多个范围的值，返回数据限制为10M。",
        "bizTag": "ccm"
    },
    {
        "name": "向单个范围写入数据",
        "detail": "根据 spreadsheetToken 和 range 向单个范围写入数据，若范围内有数据，将被更新覆盖；单次写入不超过5000行，100列，每个格子不超过5万字符。",
        "bizTag": "ccm"
    },
    {
        "name": "向多个范围写入数据",
        "detail": "根据 spreadsheetToken 和 range 向多个范围写入数据，若范围内有数据，将被更新覆盖；单次写入不超过5000行，100列，每个格子不超过5万字符。",
        "bizTag": "ccm"
    },
    {
        "name": "创建筛选",
        "detail": "在子表内创建筛选。",
        "bizTag": "ccm"
    },
    {
        "name": "更新筛选",
        "detail": "更新子表筛选范围中的列筛选条件。",
        "bizTag": "ccm"
    },
    {
        "name": "获取筛选",
        "detail": "获取子表的详细筛选信息",
        "bizTag": "ccm"
    },
    {
        "name": "删除筛选",
        "detail": "删除子表的筛选",
        "bizTag": "ccm"
    },
    {
        "name": "创建筛选视图",
        "detail": "根据传入的参数创建一个筛选视图。Id 和 名字可选，不填的话会默认生成；range 必填。Id 长度为10，由 0-9、a-z、A-Z 组合生成。名字长度不超过100。单个子表内的筛选视图个数不超过 150。",
        "bizTag": "ccm"
    },
    {
        "name": "更新筛选视图",
        "detail": "更新筛选视图的名字或者筛选范围。名字长度不超过100，不能重复即子表内唯一；筛选范围不超过子表的最大范围。",
        "bizTag": "ccm"
    },
    {
        "name": "查询筛选视图",
        "detail": "查询子表内所有的筛选视图基本信息，包括 id、name 和 range",
        "bizTag": "ccm"
    },
    {
        "name": "获取筛选视图",
        "detail": "获取指定筛选视图 id 的名字和筛选范围。",
        "bizTag": "ccm"
    },
    {
        "name": "删除筛选视图",
        "detail": "删除指定 id 对应的筛选视图。",
        "bizTag": "ccm"
    },
    {
        "name": "创建筛选条件",
        "detail": "在筛选视图的筛选范围的某一列创建筛选条件。",
        "bizTag": "ccm"
    },
    {
        "name": "更新筛选条件",
        "detail": "更新筛选视图范围的某列的筛选条件，condition id 即为列的字母号。",
        "bizTag": "ccm"
    },
    {
        "name": "查询筛选条件",
        "detail": "查询一个筛选视图的所有筛选条件，返回筛选视图的筛选范围内的筛选条件。",
        "bizTag": "ccm"
    },
    {
        "name": "获取筛选条件",
        "detail": "获取筛选视图某列的筛选条件信息。",
        "bizTag": "ccm"
    },
    {
        "name": "删除筛选条件",
        "detail": "删除筛选视图的筛选范围某一列的筛选条件。",
        "bizTag": "ccm"
    },
    {
        "name": "增加保护范围",
        "detail": "根据 spreadsheetToken 和维度信息增加多个保护范围；单次操作不超过5000行或列。",
        "bizTag": "ccm"
    },
    {
        "name": "修改保护范围",
        "detail": "根据保护范围ID修改保护范围，单次最多支持同时修改10个ID。",
        "bizTag": "ccm"
    },
    {
        "name": "获取保护范围",
        "detail": "根据保护范围ID查询详细的保护行列信息，最多支持同时查询5个ID。",
        "bizTag": "ccm"
    },
    {
        "name": "删除保护范围",
        "detail": "根据保护范围ID删除保护范围，最多支持同时删除10个ID。",
        "bizTag": "ccm"
    },
    {
        "name": "设置下拉列表",
        "detail": "根据 spreadsheetToken 、range 和下拉列表属性给单元格设置下拉列表规则；单次设置范围不超过5000行，100列。当一个数据区域中已有数据，支持将有效数据直接转为选项。",
        "bizTag": "ccm"
    },
    {
        "name": "更新下拉列表设置",
        "detail": "根据 spreadsheetToken 、sheetId、dataValidationId 更新下拉列表的属性。",
        "bizTag": "ccm"
    },
    {
        "name": "查询下拉列表设置",
        "detail": "根据 spreadsheetToken 、range 查询range内的下拉列表设置信息；单次查询范围不超过5000行，100列。",
        "bizTag": "ccm"
    },
    {
        "name": "删除下拉列表设置",
        "detail": "根据 spreadsheetToken 、range 移除选定数据范围单元格的下拉列表设置，但保留选项文本。单个删除范围不超过5000单元格。单次请求range最大数量100个。",
        "bizTag": "ccm"
    },
    {
        "name": "批量创建条件格式",
        "detail": "创建新的条件格式，单次最多支持增加10个条件格式，每个条件格式的设置会返回成功或者失败，失败的情况包括各种参数的校验。",
        "bizTag": "ccm"
    },
    {
        "name": "批量更新条件格式",
        "detail": "更新已有的条件格式，单次最多支持更新10个条件格式，每个条件格式的更新会返回成功或者失败，失败的情况包括各种参数的校验。",
        "bizTag": "ccm"
    },
    {
        "name": "批量获取条件格式",
        "detail": "根据sheetId查询详细的条件格式信息，最多支持同时查询10个sheetId。",
        "bizTag": "ccm"
    },
    {
        "name": "批量删除条件格式",
        "detail": "删除已有的条件格式，单次最多支持删除10个条件格式，每个条件格式的删除会返回成功或者失败，失败的情况包括各种参数的校验。",
        "bizTag": "ccm"
    },
    {
        "name": "创建浮动图片",
        "detail": "根据传入的参数创建一张浮动图片。Float_image_token （[上传图片至表格后得到](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all)）和range（只支持一个单元格） 必填。Float_image_id 可选，不填的话会默认生成，长度为10，由 0-9、a-z、A-Z 组合生成。表格内不重复的图片（浮动图片+单元格图片）总数不超过4000。width 和 height 为图片展示的宽高，可选，不填的话会使用图片的真实宽高。offset_x 和 offset_y 为图片左上角距离所在单元格左上角的偏移，可选，默认为 0。",
        "bizTag": "ccm"
    },
    {
        "name": "更新浮动图片",
        "detail": "更新已有的浮动图片位置和宽高，包括 range、width、height、offset_x 和 offset_y，不包括 float_image_id 和 float_image_token。",
        "bizTag": "ccm"
    },
    {
        "name": "获取浮动图片",
        "detail": "根据 float_image_id 获取对应浮动图片的信息。",
        "bizTag": "ccm"
    },
    {
        "name": "查询浮动图片",
        "detail": "返回子表内所有的浮动图片信息。",
        "bizTag": "ccm"
    },
    {
        "name": "删除浮动图片",
        "detail": "删除 float_image_id 对应的浮动图片。",
        "bizTag": "ccm"
    },
    {
        "name": "创建多维表格",
        "detail": "在指定目录下创建多维表格",
        "bizTag": "base"
    },
    {
        "name": "复制多维表格",
        "detail": "复制一个多维表格，可以指定复制到某个有权限的文件夹下",
        "bizTag": "base"
    },
    {
        "name": "获取多维表格元数据",
        "detail": "获取指定多维表格的元数据信息，包括多维表格名称，多维表格版本号，多维表格是否开启高级权限等。",
        "bizTag": "base"
    },
    {
        "name": "更新多维表格元数据",
        "detail": "通过 app_token 更新多维表格元数据",
        "bizTag": "base"
    },
    {
        "name": "新增一个数据表",
        "detail": "通过该接口，可以新增一个仅包含索引列的空数据表，也可以指定一部分初始字段。",
        "bizTag": "base"
    },
    {
        "name": "新增多个数据表",
        "detail": "新增多个数据表。",
        "bizTag": "base"
    },
    {
        "name": "更新数据表",
        "detail": "该接口用于更新数据表的基本信息，包括数据表的名称等。",
        "bizTag": "base"
    },
    {
        "name": "列出数据表",
        "detail": "根据  app_token，获取多维表格下的所有数据表。",
        "bizTag": "base"
    },
    {
        "name": "删除一个数据表",
        "detail": "删除一个数据表，最后一张数据表不允许被删除。",
        "bizTag": "base"
    },
    {
        "name": "删除多个数据表",
        "detail": "删除多个数据表。",
        "bizTag": "base"
    },
    {
        "name": "新增视图",
        "detail": "在数据表中新增一个视图",
        "bizTag": "base"
    },
    {
        "name": "更新视图",
        "detail": "该接口用于增量修改视图信息",
        "bizTag": "base"
    },
    {
        "name": "列出视图",
        "detail": "根据 app_token 和 table_id，获取数据表的所有视图",
        "bizTag": "base"
    },
    {
        "name": "获取视图",
        "detail": "该接口根据 view_id 检索现有视图",
        "bizTag": "base"
    },
    {
        "name": "删除视图",
        "detail": "删除数据表中的视图",
        "bizTag": "base"
    },
    {
        "name": "新增记录",
        "detail": "该接口用于在数据表中新增一条记录",
        "bizTag": "base"
    },
    {
        "name": "更新记录",
        "detail": "该接口用于更新数据表中的一条记录",
        "bizTag": "base"
    },
    {
        "name": "查询记录",
        "detail": "",
        "bizTag": "base"
    },
    {
        "name": "删除记录",
        "detail": "该接口用于删除数据表中的一条记录",
        "bizTag": "base"
    },
    {
        "name": "新增多条记录",
        "detail": "该接口用于在数据表中新增多条记录，单次调用最多新增 500 条记录。",
        "bizTag": "base"
    },
    {
        "name": "更新多条记录",
        "detail": "该接口用于更新数据表中的多条记录，单次调用最多更新 500 条记录。",
        "bizTag": "base"
    },
    {
        "name": "批量获取记录",
        "detail": "",
        "bizTag": "base"
    },
    {
        "name": "删除多条记录",
        "detail": "该接口用于删除数据表中现有的多条记录，单次调用中最多删除 500 条记录。",
        "bizTag": "base"
    },
    {
        "name": "新增字段",
        "detail": "该接口用于在数据表中新增一个字段",
        "bizTag": "base"
    },
    {
        "name": "更新字段",
        "detail": "该接口用于在数据表中更新一个字段",
        "bizTag": "base"
    },
    {
        "name": "列出字段",
        "detail": "根据 app_token 和 table_id，获取数据表的所有字段",
        "bizTag": "base"
    },
    {
        "name": "删除字段",
        "detail": "该接口用于在数据表中删除一个字段",
        "bizTag": "base"
    },
    {
        "name": "复制仪表盘",
        "detail": "该接口用于根据现有仪表盘复制出新的仪表盘",
        "bizTag": "base"
    },
    {
        "name": "列出仪表盘",
        "detail": "根据 app_token，获取多维表格下的所有仪表盘",
        "bizTag": "base"
    },
    {
        "name": "更新表单元数据",
        "detail": "该接口用于更新表单中的元数据项",
        "bizTag": "base"
    },
    {
        "name": "获取表单元数据",
        "detail": "获取表单的所有元数据项",
        "bizTag": "base"
    },
    {
        "name": "更新表单问题",
        "detail": "该接口用于更新表单中的问题项",
        "bizTag": "base"
    },
    {
        "name": "列出表单问题",
        "detail": "列出表单的所有问题项",
        "bizTag": "base"
    },
    {
        "name": "新增自定义角色",
        "detail": "新增自定义角色",
        "bizTag": "base"
    },
    {
        "name": "更新自定义角色",
        "detail": "更新自定义角色",
        "bizTag": "base"
    },
    {
        "name": "列出自定义角色",
        "detail": "列出自定义角色",
        "bizTag": "base"
    },
    {
        "name": "删除自定义角色",
        "detail": "删除自定义角色",
        "bizTag": "base"
    },
    {
        "name": "新增协作者",
        "detail": "新增自定义角色的协作者",
        "bizTag": "base"
    },
    {
        "name": "批量新增协作者",
        "detail": "批量新增自定义角色的协作者",
        "bizTag": "base"
    },
    {
        "name": "列出协作者",
        "detail": "列出自定义角色的协作者",
        "bizTag": "base"
    },
    {
        "name": "删除协作者",
        "detail": "删除自定义角色的协作者",
        "bizTag": "base"
    },
    {
        "name": "批量删除协作者",
        "detail": "批量删除自定义角色的协作者",
        "bizTag": "base"
    },
    {
        "name": "列出自动化流程",
        "detail": "",
        "bizTag": "base"
    },
    {
        "name": "更新自动化流程状态",
        "detail": "",
        "bizTag": "base"
    },
    {
        "name": "获取所有节点",
        "detail": "",
        "bizTag": "board"
    },
    {
        "name": "获取画板缩略图片",
        "detail": "",
        "bizTag": "board"
    },
    {
        "name": "批量增加协作者权限",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "转移所有者",
        "detail": "该接口用于根据 filetoken 和用户信息转移文件的所有者。",
        "bizTag": "ccm"
    },
    {
        "name": "判断当前用户是否有某权限",
        "detail": "该接口用于根据 filetoken 判断当前登录用户是否具有某权限。",
        "bizTag": "ccm"
    },
    {
        "name": "获取协作者列表",
        "detail": "该接口用于根据 filetoken 查询协作者",
        "bizTag": "ccm"
    },
    {
        "name": "获取协作者列表",
        "detail": "根据 filetoken 查询协作者，目前包括人(\"user\")和群(\"chat\") 。",
        "bizTag": "ccm"
    },
    {
        "name": "增加协作者权限",
        "detail": "该接口用于根据 filetoken 给用户增加文档的权限。",
        "bizTag": "ccm"
    },
    {
        "name": "更新协作者权限",
        "detail": "该接口用于根据 filetoken 更新文档协作者的权限。",
        "bizTag": "ccm"
    },
    {
        "name": "移除协作者权限",
        "detail": "该接口用于根据 filetoken 移除文档协作者的权限。",
        "bizTag": "ccm"
    },
    {
        "name": "开启密码",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "刷新密码",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "关闭密码",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档权限设置",
        "detail": "该接口用于根据 filetoken 获取云文档的权限设置。",
        "bizTag": "ccm"
    },
    {
        "name": "更新云文档权限设置",
        "detail": "该接口用于根据 filetoken 更新云文档的权限设置。",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档权限设置",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "更新云文档权限设置",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档所有评论",
        "detail": "该接口用于根据文档 token 分页获取文档评论。",
        "bizTag": "ccm"
    },
    {
        "name": "批量获取评论",
        "detail": "该接口用于根据评论 ID 列表批量获取评论。",
        "bizTag": "ccm"
    },
    {
        "name": "解决/恢复评论",
        "detail": "解决或恢复云文档中的评论。",
        "bizTag": "ccm"
    },
    {
        "name": "添加全文评论",
        "detail": "往云文档添加一条全局评论。",
        "bizTag": "ccm"
    },
    {
        "name": "获取全文评论",
        "detail": "获取云文档中的某条评论。",
        "bizTag": "ccm"
    },
    {
        "name": "获取回复信息",
        "detail": "该接口用于根据评论 ID 以及分页参数，获取回复。",
        "bizTag": "ccm"
    },
    {
        "name": "更新回复的内容",
        "detail": "更新云文档中的某条回复。",
        "bizTag": "ccm"
    },
    {
        "name": "删除回复",
        "detail": "删除云文档中的某条回复。",
        "bizTag": "ccm"
    },
    {
        "name": "获取订阅状态",
        "detail": "根据订阅ID获取该订阅的状态",
        "bizTag": "ccm"
    },
    {
        "name": "创建订阅",
        "detail": "订阅文档中的变更事件，当前支持文档评论订阅，订阅后文档评论更新会有“云文档助手”推送给订阅的用户",
        "bizTag": "ccm"
    },
    {
        "name": "更新订阅状态",
        "detail": "根据订阅ID更新订阅状态",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档内容",
        "detail": "",
        "bizTag": "ccm"
    },
    {
        "name": "创建共享日历",
        "detail": "该接口用于为当前身份（应用 / 用户）创建一个共享日历。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "删除共享日历",
        "detail": "该接口用于以当前身份（应用 / 用户）删除一个共享日历。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "查询主日历信息",
        "detail": "获取当前身份的主日历信息。",
        "bizTag": "calendar"
    },
    {
        "name": "查询日历信息",
        "detail": "该接口用于以当前身份（应用 / 用户）根据日历 ID 获取日历信息。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "查询主日历日程忙闲信息",
        "detail": "查询用户主日历或会议室的忙闲信息。",
        "bizTag": "calendar"
    },
    {
        "name": "查询日历列表",
        "detail": "该接口用于分页获得当前身份（应用 / 用户）的日历列表。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "更新日历信息",
        "detail": "该接口用于以当前身份（应用 / 用户）修改日历信息。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "搜索日历",
        "detail": "该接口用于通过关键字查询公共日历或用户主日历。",
        "bizTag": "calendar"
    },
    {
        "name": "订阅日历",
        "detail": "该接口用于以当前身份（应用 / 用户）订阅某个日历。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "取消订阅日历",
        "detail": "该接口用于以当前身份（应用 / 用户）取消对某日历的订阅状态。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "订阅日历变更事件",
        "detail": "该接口用于以用户身份订阅当前身份下日历列表中的所有日历变更。",
        "bizTag": "calendar"
    },
    {
        "name": "取消订阅日历变更事件",
        "detail": "该接口用于以用户身份取消订阅当前身份下日历列表中的日历变更事件。",
        "bizTag": "calendar"
    },
    {
        "name": "创建访问控制",
        "detail": "该接口用于以当前身份（应用 / 用户）给日历添加访问控制权限，即日历成员。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "删除访问控制",
        "detail": "该接口用于以当前身份（应用 / 用户）删除日历的控制权限，即日历成员。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "获取访问控制列表",
        "detail": "该接口用于以当前身份（应用 / 用户）获取日历的控制权限列表。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "订阅日历访问控制变更事件",
        "detail": "该接口用于以用户身份订阅指定日历下的日历成员变更事件。",
        "bizTag": "calendar"
    },
    {
        "name": "取消订阅日历访问控制变更事件",
        "detail": "该接口用于以用户身份取消订阅指定日历下的日历成员变更事件。",
        "bizTag": "calendar"
    },
    {
        "name": "创建日程",
        "detail": "该接口用于以当前身份（应用 / 用户）在日历上创建一个日程。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "删除日程",
        "detail": "该接口用于以当前身份（应用 / 用户）删除日历上的一个日程。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "更新日程",
        "detail": "该接口用于以当前身份（应用 / 用户）更新日历上的一个日程。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "获取日程",
        "detail": "该接口用于以当前身份（应用 / 用户）获取日历上的一个日程。\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "获取日程列表",
        "detail": "该接口用于以当前身份（应用 / 用户）获取日历下的日程列表。\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "搜索日程",
        "detail": "该接口用于以用户身份搜索某日历下的相关日程。\n\n身份由 Header Authorization 的 Token 类型决定。",
        "bizTag": "calendar"
    },
    {
        "name": "订阅日程变更事件",
        "detail": "该接口用于以用户身份订阅指定日历下的日程变更事件。",
        "bizTag": "calendar"
    },
    {
        "name": "取消订阅日程变更事件",
        "detail": "该接口用于以用户身份取消订阅指定日历下的日程变更事件。",
        "bizTag": "calendar"
    },
    {
        "name": "回复日程",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "获取重复日程实例",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "查询日程视图",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "创建会议群",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "解绑会议群",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "创建会议纪要",
        "detail": "",
        "bizTag": "calendar"
    },
    {
        "name": "创建请假日程",
        "detail": "为指定用户创建一个请假日程，可以是一个普通请假日程，也可以是一个全天日程。\n创建请假日程后，会在相应时间内，在用户个人签名页展示请假信息。",
        "bizTag": "calendar"
    },
    {
        "name": "删除请假日程",
        "detail": "删除一个指定的请假日程，请假日程删除，用户个人签名页的请假信息也会消失。\n一个应用只能删除自己创建的请假日程。",
        "bizTag": "calendar"
    },
    {
        "name": "查询会议室日程主题和会议详情",
        "detail": "通过日程的Uid和Original time，查询会议室日程主题。 ",
        "bizTag": "meeting_room"
    },
    {
        "name": "查询会议室忙闲",
        "detail": "获取指定会议室的忙闲日程实例列表。非重复日程只有唯一实例；重复日程可能存在多个实例，依据重复规则和时间范围扩展。",
        "bizTag": "meeting_room"
    },
    {
        "name": "回复会议室日程实例",
        "detail": "回复会议室日程实例，包括未签到释放和提前结束释放。",
        "bizTag": "meeting_room"
    },
    {
        "name": "添加日程参与人",
        "detail": "批量给日程添加参与人。",
        "bizTag": "calendar"
    },
    {
        "name": "删除日程参与人",
        "detail": "批量删除日程的参与人。",
        "bizTag": "calendar"
    },
    {
        "name": "获取日程参与人列表",
        "detail": "获取日程的参与人列表，若参与者列表中有群组，请使用 [获取参与人群成员列表](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/calendar-v4/calendar-event-attendee-chat_member/list) 。",
        "bizTag": "calendar"
    },
    {
        "name": "获取日程参与群成员列表",
        "detail": "获取日程的群参与人的群成员列表。",
        "bizTag": "calendar"
    },
    {
        "name": "生成 CalDAV 配置",
        "detail": "用于为当前用户生成一个CalDAV账号密码，用于将飞书日历信息同步到本地设备日历。",
        "bizTag": "calendar"
    },
    {
        "name": "将 Exchange 账户绑定到飞书账户",
        "detail": "本接口将Exchange账户绑定到飞书账户，进而支持Exchange日历的导入",
        "bizTag": "calendar"
    },
    {
        "name": "解除 Exchange 账户绑定",
        "detail": "本接口解除Exchange账户和飞书账户的绑定关系，Exchange账户解除绑定后才能绑定其他飞书账户",
        "bizTag": "calendar"
    },
    {
        "name": "查询 Exchange 账户的绑定状态",
        "detail": "本接口获取Exchange账户的绑定状态，包括exchange日历是否同步完成。",
        "bizTag": "calendar"
    },
    {
        "name": "预约会议",
        "detail": "创建一个会议预约。",
        "bizTag": "vc"
    },
    {
        "name": "删除预约",
        "detail": "删除一个预约。",
        "bizTag": "vc"
    },
    {
        "name": "更新预约",
        "detail": "更新一个预约。",
        "bizTag": "vc"
    },
    {
        "name": "获取预约",
        "detail": "获取一个预约的详情。",
        "bizTag": "vc"
    },
    {
        "name": "获取活跃会议",
        "detail": "获取一个预约的当前活跃会议。",
        "bizTag": "vc"
    },
    {
        "name": "邀请参会人",
        "detail": "邀请参会人进入会议。",
        "bizTag": "vc"
    },
    {
        "name": "移除参会人",
        "detail": "将参会人从会议中移除。",
        "bizTag": "vc"
    },
    {
        "name": "设置主持人",
        "detail": "设置会议的主持人。",
        "bizTag": "vc"
    },
    {
        "name": "结束会议",
        "detail": "结束一个进行中的会议。",
        "bizTag": "vc"
    },
    {
        "name": "获取会议详情",
        "detail": "获取一个会议的详细数据。",
        "bizTag": "vc"
    },
    {
        "name": "获取与会议号关联的会议列表",
        "detail": "获取指定时间范围（90天内)会议号关联的会议简要信息列表。",
        "bizTag": "vc"
    },
    {
        "name": "开始录制",
        "detail": "在会议中开始录制。",
        "bizTag": "vc"
    },
    {
        "name": "停止录制",
        "detail": "在会议中停止录制。",
        "bizTag": "vc"
    },
    {
        "name": "获取录制文件",
        "detail": "获取一个会议的录制文件。",
        "bizTag": "vc"
    },
    {
        "name": "授权录制文件",
        "detail": "将一个会议的录制文件授权给组织、用户或公开到公网。",
        "bizTag": "vc"
    },
    {
        "name": "获取会议报告",
        "detail": "获取一段时间内组织的每日会议使用报告。",
        "bizTag": "vc"
    },
    {
        "name": "获取 Top 用户列表",
        "detail": "获取一段时间内组织内会议使用的 Top 用户列表。",
        "bizTag": "vc"
    },
    {
        "name": "导出会议明细",
        "detail": "导出会议明细，具体权限要求请参考资源介绍。",
        "bizTag": "vc"
    },
    {
        "name": "导出参会人明细",
        "detail": "导出某个会议的参会人详情列表，具体权限要求请参考「资源介绍」。",
        "bizTag": "vc"
    },
    {
        "name": "导出参会人会议质量数据",
        "detail": "导出某场会议某个参会人的音视频&共享质量数据\n，具体权限要求请参考「资源介绍」。",
        "bizTag": "vc"
    },
    {
        "name": "导出会议室预定数据",
        "detail": "导出会议室预定数据，具体权限要求请参考「资源介绍」。",
        "bizTag": "vc"
    },
    {
        "name": "查询导出任务结果",
        "detail": "查看异步导出的进度。",
        "bizTag": "vc"
    },
    {
        "name": "下载导出文件",
        "detail": "下载导出文件。",
        "bizTag": "vc"
    },
    {
        "name": "创建会议室层级",
        "detail": "该接口用于创建会议室层级。",
        "bizTag": "vc"
    },
    {
        "name": "删除会议室层级",
        "detail": "该接口可以用来删除某个会议室层级。",
        "bizTag": "vc"
    },
    {
        "name": "更新会议室层级",
        "detail": "该接口可以用来更新某个会议室层级的信息。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室层级详情",
        "detail": "该接口可以使用会议室层级 ID 查询会议室层级详情。",
        "bizTag": "vc"
    },
    {
        "name": "批量查询会议室层级详情",
        "detail": "该接口可以使用会议室层级 ID 批量查询会议室层级详情。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室层级列表",
        "detail": "该接口用来查询某个会议室层级下的子层级列表。",
        "bizTag": "vc"
    },
    {
        "name": "搜索会议室层级",
        "detail": "该接口可以用来搜索会议室层级，支持使用自定义会议室层级 ID 进行查询。",
        "bizTag": "vc"
    },
    {
        "name": "创建会议室",
        "detail": "该接口用于创建会议室。",
        "bizTag": "vc"
    },
    {
        "name": "删除会议室",
        "detail": "该接口可以用来删除某个会议室。",
        "bizTag": "vc"
    },
    {
        "name": "更新会议室",
        "detail": "该接口可以用来更新某个会议室的信息。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室详情",
        "detail": "该接口可以使用会议室 ID 查询会议室详情。",
        "bizTag": "vc"
    },
    {
        "name": "批量查询会议室详情",
        "detail": "该接口可以使用会议室 ID 批量查询会议室详情。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室列表",
        "detail": "该接口可以用来查询某个会议室层级下会议室列表。",
        "bizTag": "vc"
    },
    {
        "name": "搜索会议室",
        "detail": "该接口可以用来搜索会议室，支持使用关键词进行搜索，也支持使用自定义会议室 ID 进行查询。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室配置",
        "detail": "该接口可以用来查询某个会议层级范围下或者某个会议室的配置。",
        "bizTag": "vc"
    },
    {
        "name": "设置会议室配置",
        "detail": "该接口可以用来设置某个会议层级范围下或者某个会议室的配置。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室预定限制",
        "detail": "查询会议室预定限制。",
        "bizTag": "vc"
    },
    {
        "name": "更新会议室预定限制",
        "detail": "更新会议室预定限制。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室预定表单",
        "detail": "查询会议室预定表单。",
        "bizTag": "vc"
    },
    {
        "name": "更新会议室预定表单",
        "detail": "更新会议室预定表单。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室预定管理员",
        "detail": "查询会议室预定管理员。",
        "bizTag": "vc"
    },
    {
        "name": "更新会议室预定管理员",
        "detail": "更新会议室预定管理员。",
        "bizTag": "vc"
    },
    {
        "name": "查询禁用状态变更通知",
        "detail": "查询禁用状态变更通知",
        "bizTag": "vc"
    },
    {
        "name": "更新禁用状态变更通知",
        "detail": "更新禁用状态变更通知",
        "bizTag": "vc"
    },
    {
        "name": "查询会议明细",
        "detail": "查询会议明细。",
        "bizTag": "vc"
    },
    {
        "name": "查询参会人明细",
        "detail": "查询参会人明细。",
        "bizTag": "vc"
    },
    {
        "name": "查询参会人会议质量数据",
        "detail": "查询参会人会议质量数据。",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室预定数据",
        "detail": "查询会议室预定数据。",
        "bizTag": "vc"
    },
    {
        "name": "获取告警记录",
        "detail": "获取特定条件下租户的设备告警记录。",
        "bizTag": "vc"
    },
    {
        "name": "创建班次",
        "detail": "班次是描述一次考勤任务时间规则的统称，比如一天打多少次卡，每次卡的上下班时间，晚到多长时间算迟到，晚到多长时间算缺卡等。",
        "bizTag": "attendance"
    },
    {
        "name": "删除班次",
        "detail": "通过班次 ID 删除班次。",
        "bizTag": "attendance"
    },
    {
        "name": "按 ID 查询班次",
        "detail": "通过班次 ID 获取班次详情。",
        "bizTag": "attendance"
    },
    {
        "name": "按名称查询班次",
        "detail": "通过班次的名称查询班次信息。",
        "bizTag": "attendance"
    },
    {
        "name": "查询所有班次",
        "detail": "翻页获取所有班次列表。",
        "bizTag": "attendance"
    },
    {
        "name": "创建或修改排班表",
        "detail": "班表是用来描述考勤组内人员每天按哪个班次进行上班。目前班表支持按一个整月对一位或多位人员进行排班。",
        "bizTag": "attendance"
    },
    {
        "name": "查询排班表",
        "detail": "支持查询多个用户的排班情况，查询的时间跨度不能超过 30 天。",
        "bizTag": "attendance"
    },
    {
        "name": "创建或修改临时排班",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "查询考勤组下所有成员",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "创建或修改考勤组",
        "detail": "考勤组，是对部门或者员工在某个特定场所及特定时间段内的出勤情况（包括上下班、迟到、早退、病假、婚假、丧假、公休、工作时间、加班情况等）的一种规则设定。\n\n通过设置考勤组，可以从部门、员工两个维度，来设定考勤方式、考勤时间、考勤地点等考勤规则。",
        "bizTag": "attendance"
    },
    {
        "name": "删除考勤组",
        "detail": "通过班次 ID 删除班次。",
        "bizTag": "attendance"
    },
    {
        "name": "按 ID 查询考勤组",
        "detail": "通过考勤组 ID 获取考勤组详情。",
        "bizTag": "attendance"
    },
    {
        "name": "按名称查询考勤组",
        "detail": "按考勤组名称查询考勤组摘要信息。查询条件支持名称精确匹配和模糊匹配两种方式。查询结果按考勤组修改时间 desc 排序，且最大记录数为 10 条。",
        "bizTag": "attendance"
    },
    {
        "name": "查询所有考勤组",
        "detail": "翻页获取所有考勤组列表。",
        "bizTag": "attendance"
    },
    {
        "name": "修改用户人脸识别信息",
        "detail": "修改授权内员工的用户设置信息，包括人脸照片文件 ID。",
        "bizTag": "attendance"
    },
    {
        "name": "批量查询用户人脸识别信息",
        "detail": "批量查询授权内员工的用户设置信息，包括人脸照片文件 ID、人脸照片更新时间。",
        "bizTag": "attendance"
    },
    {
        "name": "上传用户人脸识别照片",
        "detail": "上传文件并获取文件 ID，可用于“修改用户设置”接口中的 face_key 参数。",
        "bizTag": "attendance"
    },
    {
        "name": "下载用户人脸识别照片",
        "detail": "通过文件 ID 下载指定的文件。",
        "bizTag": "attendance"
    },
    {
        "name": "更新统计设置",
        "detail": "更新开发者定制的日度统计或月度统计的统计报表表头设置信息。",
        "bizTag": "attendance"
    },
    {
        "name": "查询统计表头",
        "detail": "查询考勤统计支持的日度统计或月度统计的统计表头。",
        "bizTag": "attendance"
    },
    {
        "name": "查询统计设置",
        "detail": "查询开发者定制的日度统计或月度统计的统计报表表头设置信息。",
        "bizTag": "attendance"
    },
    {
        "name": "查询统计数据",
        "detail": "查询日度统计或月度统计的统计数据。",
        "bizTag": "attendance"
    },
    {
        "name": "获取审批数据",
        "detail": "获取员工在某段时间内的请假、加班、外出和出差四种审批的通过数据。",
        "bizTag": "attendance"
    },
    {
        "name": "写入审批结果",
        "detail": "由于部分企业使用的是自己的审批系统，而不是飞书审批系统，因此员工的请假、加班等数据无法流入到飞书考勤系统中，导致员工在请假时间段内依然收到打卡提醒，并且被记为缺卡。\n\n对于这些只使用飞书考勤系统，而未使用飞书审批系统的企业，可以通过考勤开放接口的形式，将三方审批结果数据回写到飞书考勤系统中。",
        "bizTag": "attendance"
    },
    {
        "name": "通知审批状态更新",
        "detail": "对于只使用飞书考勤系统而未使用飞书审批系统的企业，可以通过该接口更新写入飞书考勤系统中的三方系统审批状态，例如请假、加班、外出、出差、补卡等审批，状态包括通过、不通过、撤销等。",
        "bizTag": "attendance"
    },
    {
        "name": "通知补卡审批发起",
        "detail": "对于只使用飞书考勤系统而未使用飞书审批系统的企业，可以通过该接口，将在三方审批系统中发起的补卡审批数据，写入到飞书考勤系统中，状态为审批中。写入后可以由[通知审批状态更新](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/attendance-v1/approval_info/process) 进行状态更新",
        "bizTag": "attendance"
    },
    {
        "name": "获取可补卡时间",
        "detail": "获取用户某天可以补的第几次上 / 下班卡的时间。",
        "bizTag": "attendance"
    },
    {
        "name": "获取补卡记录",
        "detail": "获取授权内员工的补卡记录。",
        "bizTag": "attendance"
    },
    {
        "name": "查询归档报表表头",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "写入归档报表结果",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "删除归档报表行数据",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "查询所有归档规则",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "导入打卡流水",
        "detail": "导入授权内员工的打卡流水记录。导入后，会根据员工所在的考勤组班次规则，计算最终的打卡状态与结果。",
        "bizTag": "attendance"
    },
    {
        "name": "查询打卡流水",
        "detail": "通过打卡记录 ID 获取用户的打卡流水记录。",
        "bizTag": "attendance"
    },
    {
        "name": "批量查询打卡流水",
        "detail": "批量查询授权内员工的实际打卡流水记录。例如，企业给一个员工设定的班次是上午 9 点和下午 6 点各打一次上下班卡，但是该员工在这期间打了多次卡，该接口会把所有的打卡记录都返回。",
        "bizTag": "attendance"
    },
    {
        "name": "查询打卡结果",
        "detail": "获取企业内员工的实际打卡结果，包括上班打卡结果和下班打卡结果。",
        "bizTag": "attendance"
    },
    {
        "name": "通过过期时间获取发放记录",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "修改发放记录",
        "detail": "",
        "bizTag": "attendance"
    },
    {
        "name": "创建审批定义",
        "detail": "用于通过接口创建简单的审批定义，可以灵活指定定义的基础信息、表单和流程等。创建成功后，不支持从审批管理后台删除该定义。不推荐企业自建应用使用，如有需要尽量联系管理员在审批管理后台创建定义。",
        "bizTag": "approval"
    },
    {
        "name": "查看指定审批定义",
        "detail": "根据 Approval Code 获取某个审批定义的详情，用于构造创建审批实例的请求。",
        "bizTag": "approval"
    },
    {
        "name": "创建审批实例",
        "detail": "创建一个审批实例，调用方需对审批定义的表单有详细了解，将按照定义的表单结构，将表单 Value 通过接口传入。",
        "bizTag": "approval"
    },
    {
        "name": "撤回审批实例",
        "detail": "对于状态为“审批中”的单个审批实例进行撤销操作，撤销后审批流程结束。",
        "bizTag": "approval"
    },
    {
        "name": "抄送审批实例",
        "detail": "通过接口可以将当前审批实例抄送给其他人。",
        "bizTag": "approval"
    },
    {
        "name": "预览审批流程",
        "detail": "提交审批前，预览审批流程。或者发起审批后，在某一审批节点预览后续流程。",
        "bizTag": "approval"
    },
    {
        "name": "获取单个审批实例详情",
        "detail": "通过审批实例 Instance Code  获取审批实例详情。Instance Code 由 [批量获取审批实例](/ssl:ttdoc/uAjLw4CM/ukTMukTMukTM/reference/approval-v4/instance/list) 接口获取。",
        "bizTag": "approval"
    },
    {
        "name": "批量获取审批实例 ID",
        "detail": "根据 approval_code 批量获取审批实例的 instance_code，用于拉取租户下某个审批定义的全部审批实例。默认以审批创建时间先后顺序排列。",
        "bizTag": "approval"
    },
    {
        "name": "同意审批任务",
        "detail": "对于单个审批任务进行同意操作。同意后审批流程会流转到下一个审批人。",
        "bizTag": "approval"
    },
    {
        "name": "拒绝审批任务",
        "detail": "对于单个审批任务进行拒绝操作。拒绝后审批流程结束。",
        "bizTag": "approval"
    },
    {
        "name": "转交审批任务",
        "detail": "对于单个审批任务进行转交操作。转交后审批流程流转给被转交人。",
        "bizTag": "approval"
    },
    {
        "name": "退回审批任务",
        "detail": "从当前审批任务，退回到已审批的一个或多个任务节点。退回后，已审批节点重新生成审批任务。",
        "bizTag": "approval"
    },
    {
        "name": "审批任务加签",
        "detail": "对于单个审批任务进行加签操作。",
        "bizTag": "approval"
    },
    {
        "name": "重新提交审批任务",
        "detail": "对于单个退回到发起人的审批任务进行重新发起操作。发起后审批流程会流转到下一个审批人。",
        "bizTag": "approval"
    },
    {
        "name": "上传文件",
        "detail": "当审批表单中有图片或附件控件时，开发者需在创建审批实例前通过审批上传文件接口将文件上传到审批系统。",
        "bizTag": "approval"
    },
    {
        "name": "创建评论",
        "detail": "在某审批实例下创建、修改评论或评论回复（不包含审批同意、拒绝、转交等附加的理由或意见）。",
        "bizTag": "approval"
    },
    {
        "name": "删除评论",
        "detail": "逻辑删除某审批实例下的一条评论或评论回复（不包含审批同意、拒绝、转交等附加的理由或意见）。",
        "bizTag": "approval"
    },
    {
        "name": "清空评论",
        "detail": "删除某审批实例下的全部评论与评论回复。",
        "bizTag": "approval"
    },
    {
        "name": "获取评论",
        "detail": "根据 Instance Code 获取某个审批实例下的全部评论与评论回复（不包含审批同意、拒绝、转交等附加的理由或意见）。",
        "bizTag": "approval"
    },
    {
        "name": "创建三方审批定义",
        "detail": "审批定义是审批的描述，包括审批名称、图标、描述等基础信息。创建好审批定义，用户就可以在审批应用的发起页中看到审批，如果用户点击发起，则会跳转到配置的发起三方系统地址去发起审批。\n\n另外，审批定义还配置了审批操作时的回调地址：审批人在待审批列表中进行【同意】【拒绝】操作时，审批中心会调用回调地址通知三方系统。",
        "bizTag": "approval"
    },
    {
        "name": "查看指定三方审批定义",
        "detail": "",
        "bizTag": "approval"
    },
    {
        "name": "三方快捷审批回调",
        "detail": "审批人在【待审批】列表中，对审批任务进行【同意】【拒绝】操作时，审批中心会调用审批定义中配置的回调URL通知三方系统。",
        "bizTag": "approval"
    },
    {
        "name": "同步三方审批实例",
        "detail": "审批中心不负责审批的流转，审批的流转在三方系统，三方系统在审批流转后生成的审批实例、审批任务、审批抄送数据同步到审批中心。\n\n用户可以在审批中心中浏览三方系统同步过来的实例、任务、抄送信息，并且可以跳转回三方系统进行更详细的查看和操作，其中实例信息在【已发起】列表，任务信息在【待审批】和【已审批】列表，抄送信息在【抄送我】列表。\n\n:::html\n<img src=\"//sf3-cn.feishucdn.com/obj/open-platform-opendoc/9dff4434afbeb0ef69de7f36b9a6e995_z5iwmTzEgg.png\" alt=\"\" style=\"zoom:17%;\" />\n\n\n<img src=\"//sf3-cn.feishucdn.com/obj/open-platform-opendoc/ca6e0e984a7a6d64e1b16a0bac4bf868_tfqjCiaJQM.png\" alt=\"\" style=\"zoom:17%;\" />\n\n\n<img src=\"//sf3-cn.feishucdn.com/obj/open-platform-opendoc/529377e238df78d391bbd22e962ad195_T7eefLI1GA.png\" alt=\"\" style=\"zoom:17%;\" />\n:::\n\n对于审批任务，三方系统也可以配置审批任务的回调接口，这样审批人可以在审批中心中直接进行审批操作，审批中心会回调三方系统，三方系统收到回调后更新任务信息，并将新的任务信息同步回审批中心，形成闭环。\n\n:::html\n<img src=\"//sf3-cn.feishucdn.com/obj/open-platform-opendoc/721c35428bc1187db3318c572f9979ad_je75QpElcg.png\" alt=\"\"  style=\"zoom:25%;\" />\n:::\n<br>",
        "bizTag": "approval"
    },
    {
        "name": "校验三方审批实例",
        "detail": "校验三方审批实例数据，用于判断服务端数据是否为最新的。用户提交实例最新更新时间，如果服务端不存在该实例，或者服务端实例更新时间不是最新的，则返回对应实例 id。\n\n例如，用户可以每隔5分钟，将最近5分钟产生的实例使用该接口进行对比。",
        "bizTag": "approval"
    },
    {
        "name": "获取三方审批任务状态",
        "detail": "该接口用于获取三方审批的状态。用户传入查询条件，接口返回满足条件的审批实例的状态。该接口支持多种参数的组合，包括如下组合：\n\n1.通过 instance_ids 获取指定实例的任务状态\n\n2.通过 user_ids 获取指定用户的任务状态\n\n3.通过 status 获取指定状态的所有任务\n\n4.通过page_token获取下一批数据",
        "bizTag": "approval"
    },
    {
        "name": "发送审批 Bot 消息",
        "detail": "通过飞书审批的Bot推送消息给用户，当有新的审批待办，或者审批待办的状态有更新时，可以通过飞书审批的Bot告知用户。当然开发者也可以利用开放平台的能力自建一个全新的Bot，用来推送审批相关信息。",
        "bizTag": "approval"
    },
    {
        "name": "更新审批 Bot 消息",
        "detail": "此接口可以根据审批bot消息id及相应状态，更新相应的审批bot消息，只可用于更新待审批模板的bot消息。例如，给用户推送了审批待办消息，当用户处理该消息后，可以将之前推送的Bot消息更新为已审批。",
        "bizTag": "approval"
    },
    {
        "name": "查询实例列表",
        "detail": "该接口通过不同条件查询审批系统中符合条件的审批实例列表。",
        "bizTag": "approval"
    },
    {
        "name": "查询抄送列表",
        "detail": "该接口通过不同条件查询审批系统中符合条件的审批抄送列表。",
        "bizTag": "approval"
    },
    {
        "name": "查询任务列表",
        "detail": "该接口通过不同条件查询审批系统中符合条件的审批任务列表。",
        "bizTag": "approval"
    },
    {
        "name": "查询用户的任务列表",
        "detail": "根据用户和任务分组查询任务列表。",
        "bizTag": "approval"
    },
    {
        "name": "查询审批 ID（专用）",
        "detail": "审批ID查询专用。",
        "bizTag": "approval"
    },
    {
        "name": "订阅审批事件",
        "detail": "应用订阅 approval_code 后，该应用就可以收到该审批定义对应实例的事件通知。同一应用只需要订阅一次，无需重复订阅。\n\n当应用不希望再收到审批事件时，可以使用取消订阅接口进行取消，取消后将不再给应用推送消息。\n\n订阅和取消订阅都是应用维度的，多个应用可以同时订阅同一个 approval_code，每个应用都能收到审批事件。",
        "bizTag": "approval"
    },
    {
        "name": "取消订阅审批事件",
        "detail": "取消订阅 approval_code 后，无法再收到该审批定义对应实例的事件通知",
        "bizTag": "approval"
    },
    {
        "name": "更新客服信息",
        "detail": "更新客服状态等信息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取客服邮箱",
        "detail": "该接口用于获取客服邮箱地址。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建客服工作日程",
        "detail": "该接口用于创建客服日程。",
        "bizTag": "helpdesk"
    },
    {
        "name": "删除客服工作日程",
        "detail": "该接口用于删除客服日程。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新客服工作日程",
        "detail": "该接口用于更新客服的日程。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询指定客服工作日程",
        "detail": "该接口用于获取客服信息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询全部客服工作日程",
        "detail": "该接口用于获取所有客服信息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建客服技能",
        "detail": "该接口用于创建客服技能。",
        "bizTag": "helpdesk"
    },
    {
        "name": "删除客服技能",
        "detail": "该接口用于删除客服技能。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新客服技能",
        "detail": "该接口用于更新客服技能。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询指定客服技能",
        "detail": "该接口用于获取客服技能。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询全部客服技能",
        "detail": "获取全部客服技能。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取客服技能列表",
        "detail": "该接口用于获取全部客服技能。仅支持自建应用。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建服务台对话",
        "detail": "该接口用于创建服务台对话。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询指定工单详情",
        "detail": "该接口用于获取单个服务台工单详情。仅支持自建应用。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新工单详情",
        "detail": "该接口用于更新服务台工单详情。只会更新数据，不会触发相关操作。如修改工单状态到关单，不会关闭聊天页面。仅支持自建应用。要更新的工单字段必须至少输入一项。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询全部工单详情",
        "detail": "该接口用于获取全部工单详情。仅支持自建应用。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取工单内图像",
        "detail": "该接口用于获取服务台工单消息图象。仅支持自建应用。",
        "bizTag": "helpdesk"
    },
    {
        "name": "回复用户在工单里的提问",
        "detail": "该接口用于回复用户提问结果至工单，需要工单仍处于进行中且未接入人工状态。仅支持自建应用。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取服务台自定义字段",
        "detail": "该接口用于获取服务台自定义字段详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "发送工单消息",
        "detail": "该接口用于发送工单消息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取工单消息详情",
        "detail": "该接口用于获取服务台工单消息详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "服务台机器人向工单绑定的群内发送消息",
        "detail": "通过服务台机器人给指定用户的服务台专属群或私聊发送消息，支持文本、富文本、卡片、图片。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建工单自定义字段",
        "detail": "该接口用于创建自定义字段",
        "bizTag": "helpdesk"
    },
    {
        "name": "删除工单自定义字段",
        "detail": "该接口用于删除工单自定义字段。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新工单自定义字段",
        "detail": "该接口用于更新自定义字段。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取指定工单自定义字段",
        "detail": "该接口用于获取工单自定义字段详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取全部工单自定义字段",
        "detail": "该接口用于获取全部工单自定义字段。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建知识库",
        "detail": "该接口用于创建知识库。",
        "bizTag": "helpdesk"
    },
    {
        "name": "删除知识库",
        "detail": "该接口用于删除知识库。",
        "bizTag": "helpdesk"
    },
    {
        "name": "修改知识库",
        "detail": "该接口用于修改知识库。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取指定知识库详情",
        "detail": "该接口用于获取服务台知识库详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取全部知识库详情",
        "detail": "该接口用于获取服务台知识库详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取知识库图像",
        "detail": "该接口用于获取知识库图像。",
        "bizTag": "helpdesk"
    },
    {
        "name": "搜索知识库",
        "detail": "该接口用于搜索服务台知识库。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建知识库分类",
        "detail": "该接口用于创建知识库分类。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取知识库分类",
        "detail": "该接口用于获取知识库分类。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新知识库分类详情",
        "detail": "该接口用于更新知识库分类详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "删除知识库分类详情",
        "detail": "该接口用于删除知识库分类详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "获取全部知识库分类",
        "detail": "该接口用于获取服务台知识库所有分类",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建推送",
        "detail": "调用接口创建推送，创建成功后为草稿状态。",
        "bizTag": "helpdesk"
    },
    {
        "name": "更新推送",
        "detail": "更新推送信息，只有在草稿状态下才可以调用此接口进行更新。",
        "bizTag": "helpdesk"
    },
    {
        "name": "查询推送",
        "detail": "查询推送详情。",
        "bizTag": "helpdesk"
    },
    {
        "name": "预览推送",
        "detail": "在正式执行推送之前是可以调用此接口预览设置的推送内容。",
        "bizTag": "helpdesk"
    },
    {
        "name": "提交审核",
        "detail": "正常情况下调用创建推送接口后，就可以调用提交审核接口，如果创建人是服务台owner则会自动审核通过，否则会通知服务台owner审核此推送信息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "取消审核",
        "detail": "提交审核后，如果需要取消审核，则调用此接口。",
        "bizTag": "helpdesk"
    },
    {
        "name": "执行推送",
        "detail": "审核通过后调用此接口设置推送时间，等待调度系统调度，发送消息。",
        "bizTag": "helpdesk"
    },
    {
        "name": "取消推送",
        "detail": "取消推送接口，审核通过后待调度可以调用，发送过程中可以调用（会撤回已发送的消息），发送完成后可以需要推送（会撤回所有已发送的消息）。",
        "bizTag": "helpdesk"
    },
    {
        "name": "订阅服务台事件",
        "detail": "本接口用于订阅服务台事件。",
        "bizTag": "helpdesk"
    },
    {
        "name": "取消订阅服务台事件",
        "detail": "本接口用于取消订阅服务台事件。",
        "bizTag": "helpdesk"
    },
    {
        "name": "创建任务",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取任务详情",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新任务",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除任务",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "添加任务成员",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "移除任务成员",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "列取任务列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "列取任务所在清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "任务加入清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "任务移出清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "添加任务提醒",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "移除任务提醒",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "添加依赖",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "移除依赖",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建子任务",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取任务的子任务列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取清单详情",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除清单",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "添加清单成员",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "移除清单成员",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取清单任务列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取清单列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建动态订阅",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取动态订阅",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "列取动态订阅",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新动态订阅",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除动态订阅",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建评论",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取评论详情",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新评论",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除评论",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取评论列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "上传附件",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "列取附件",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取附件",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除附件",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建自定义分组",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取自定义分组详情",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新自定义分组",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "删除自定义分组",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取自定义分组列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取自定义分组任务列表",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建自定义字段",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "获取自定义字段",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新自定义字段",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "列取自定义字段",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "将自定义字段加入资源",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "将自定义字段移出资源",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "创建自定义任务选项",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "更新自定义字段选项",
        "detail": "",
        "bizTag": "task"
    },
    {
        "name": "发送邮件",
        "detail": "发送邮件",
        "bizTag": "mail"
    },
    {
        "name": "创建邮件组",
        "detail": "创建一个邮件组",
        "bizTag": "mail"
    },
    {
        "name": "删除邮件组",
        "detail": "删除一个邮件组",
        "bizTag": "mail"
    },
    {
        "name": "修改邮件组部分信息",
        "detail": "更新邮件组部分字段，没有填写的字段不会被更新。",
        "bizTag": "mail"
    },
    {
        "name": "修改邮件组全部信息",
        "detail": "更新邮件组所有信息。",
        "bizTag": "mail"
    },
    {
        "name": "查询指定邮件组",
        "detail": "获取特定邮件组信息。",
        "bizTag": "mail"
    },
    {
        "name": "批量获取邮件组",
        "detail": "分页批量获取邮件组",
        "bizTag": "mail"
    },
    {
        "name": "批量创建邮件组管理员",
        "detail": "批量创建邮件组管理员。",
        "bizTag": "mail"
    },
    {
        "name": "批量删除邮件组管理员",
        "detail": "批量删除邮件组管理员。",
        "bizTag": "mail"
    },
    {
        "name": "批量获取邮件组管理员",
        "detail": "批量获取邮件组管理员。",
        "bizTag": "mail"
    },
    {
        "name": "创建邮件组成员",
        "detail": "向邮件组添加单个成员。",
        "bizTag": "mail"
    },
    {
        "name": "删除邮件组成员",
        "detail": "删除邮件组单个成员。",
        "bizTag": "mail"
    },
    {
        "name": "查询指定邮件组成员",
        "detail": "获取邮件组单个成员信息。",
        "bizTag": "mail"
    },
    {
        "name": "获取所有邮件组成员",
        "detail": "分页批量获取邮件组成员列表。",
        "bizTag": "mail"
    },
    {
        "name": "批量创建邮件组成员",
        "detail": "一次请求可以给一个邮件组添加多个成员。",
        "bizTag": "mail"
    },
    {
        "name": "批量删除邮件组成员",
        "detail": "一次请求可以删除一个邮件组中的多个成员。",
        "bizTag": "mail"
    },
    {
        "name": "创建邮件组别名",
        "detail": "创建邮件组别名。",
        "bizTag": "mail"
    },
    {
        "name": "删除邮件组别名",
        "detail": "删除邮件组别名。",
        "bizTag": "mail"
    },
    {
        "name": "获取邮件组所有别名",
        "detail": "获取邮件组所有别名。",
        "bizTag": "mail"
    },
    {
        "name": "创建邮件组权限成员",
        "detail": "向邮件组添加单个自定义权限成员，添加后该成员可发送邮件到该邮件组。",
        "bizTag": "mail"
    },
    {
        "name": "删除邮件组权限成员",
        "detail": "从自定义成员中删除单个成员，删除后该成员无法发送邮件到该邮件组。",
        "bizTag": "mail"
    },
    {
        "name": "获取邮件组权限成员",
        "detail": "获取邮件组单个权限成员信息。",
        "bizTag": "mail"
    },
    {
        "name": "批量获取邮件组权限成员",
        "detail": "分页批量获取邮件组权限成员列表。",
        "bizTag": "mail"
    },
    {
        "name": "批量创建邮件组权限成员",
        "detail": "一次请求可以给一个邮件组添加多个权限成员。",
        "bizTag": "mail"
    },
    {
        "name": "批量删除邮件组权限成员",
        "detail": "一次请求可以删除一个邮件组中的多个权限成员。",
        "bizTag": "mail"
    },
    {
        "name": "创建公共邮箱",
        "detail": "创建一个公共邮箱。",
        "bizTag": "mail"
    },
    {
        "name": "修改公共邮箱部分信息",
        "detail": "更新公共邮箱部分字段，没有填写的字段不会被更新。",
        "bizTag": "mail"
    },
    {
        "name": "修改公共邮箱全部信息",
        "detail": "更新公共邮箱所有信息。",
        "bizTag": "mail"
    },
    {
        "name": "查询指定公共邮箱",
        "detail": "获取公共邮箱信息。",
        "bizTag": "mail"
    },
    {
        "name": "查询所有公共邮箱",
        "detail": "分页批量获取公共邮箱列表。",
        "bizTag": "mail"
    },
    {
        "name": "永久删除公共邮箱",
        "detail": "该接口会永久删除公共邮箱地址。可用于释放邮箱回收站的公共邮箱地址，一旦删除，该邮箱地址将无法恢复。",
        "bizTag": "mail"
    },
    {
        "name": "添加公共邮箱成员",
        "detail": "向公共邮箱添加单个成员。",
        "bizTag": "mail"
    },
    {
        "name": "删除公共邮箱单个成员",
        "detail": "删除公共邮箱单个成员。",
        "bizTag": "mail"
    },
    {
        "name": "删除公共邮箱所有成员",
        "detail": "删除公共邮箱所有成员。",
        "bizTag": "mail"
    },
    {
        "name": "查询指定公共邮箱成员信息",
        "detail": "获取公共邮箱单个成员信息。",
        "bizTag": "mail"
    },
    {
        "name": "查询所有公共邮箱成员信息",
        "detail": "分页批量获取公共邮箱成员列表。",
        "bizTag": "mail"
    },
    {
        "name": "批量添加公共邮箱成员",
        "detail": "一次请求可以给一个公共邮箱添加多个成员。",
        "bizTag": "mail"
    },
    {
        "name": "批量删除公共邮箱成员",
        "detail": "一次请求可以删除一个公共邮箱中的多个成员。",
        "bizTag": "mail"
    },
    {
        "name": "创建公共邮箱别名",
        "detail": "创建公共邮箱别名。",
        "bizTag": "mail"
    },
    {
        "name": "删除公共邮箱别名",
        "detail": "删除公共邮箱别名。",
        "bizTag": "mail"
    },
    {
        "name": "查询公共邮箱的所有别名",
        "detail": "获取所有公共邮箱别名。",
        "bizTag": "mail"
    },
    {
        "name": "从回收站删除用户邮箱地址",
        "detail": "该接口会永久删除用户邮箱地址。可用于删除位于邮箱回收站中的用户邮箱地址，一旦删除，将无法恢复。该接口支持邮件的转移，可以将被释放邮箱的邮件转移到另外一个可以使用的邮箱中。",
        "bizTag": "mail"
    },
    {
        "name": "创建用户邮箱别名",
        "detail": "创建用户邮箱别名。",
        "bizTag": "mail"
    },
    {
        "name": "删除用户邮箱别名",
        "detail": "删除用户邮箱别名。",
        "bizTag": "mail"
    },
    {
        "name": "获取用户邮箱所有别名",
        "detail": "获取用户邮箱所有别名。",
        "bizTag": "mail"
    },
    {
        "name": "查询邮箱地址状态",
        "detail": "使用邮箱状态查询接口，可以输入邮箱地址，查询出该邮箱地址对应的类型以及状态。",
        "bizTag": "mail"
    },
    {
        "name": "转移应用所有者",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "更新应用协作者",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取应用协作者列表",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取应用信息",
        "detail": "根据app_id获取应用的基础信息",
        "bizTag": "application"
    },
    {
        "name": "获取应用版本信息",
        "detail": "根据应用 ID 和应用版本 ID 来获取同租户下的应用版本的信息",
        "bizTag": "application"
    },
    {
        "name": "获取应用版本列表",
        "detail": "根据 app_id 获取对应应用版本列表。",
        "bizTag": "application"
    },
    {
        "name": "获取应用版本中开发者申请的通讯录权限范围",
        "detail": "根据应用 ID 和应用版本 ID 来获取同租户下的应用版本通讯录权限范围建议的信息",
        "bizTag": "application"
    },
    {
        "name": "向管理员申请授权",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "查询租户授权状态",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取企业安装的应用",
        "detail": "该接口用于查询企业安装的应用列表，只能被企业自建应用调用。",
        "bizTag": "application"
    },
    {
        "name": "获取用户可用的应用",
        "detail": "查询用户可用的应用列表，只能被企业自建应用调用。",
        "bizTag": "application"
    },
    {
        "name": "查看待审核的应用列表",
        "detail": "查看本企业下所有待审核的自建应用列表",
        "bizTag": "application"
    },
    {
        "name": "更新应用审核状态",
        "detail": "通过接口来更新应用版本的审核结果：通过后应用可以直接上架；拒绝后则开发者可以看到拒绝理由，并在修改后再次申请发布。",
        "bizTag": "application"
    },
    {
        "name": "更新应用分组信息",
        "detail": "更新应用的分组信息（分组会影响应用在工作台中的分类情况，请谨慎更新）",
        "bizTag": "application"
    },
    {
        "name": "获取应用通讯录权限范围配置",
        "detail": "根据应用id获取通讯录权限范围配置",
        "bizTag": "application"
    },
    {
        "name": "更新应用通讯录权限范围配置",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取应用在企业内的可用范围",
        "detail": "查询应用在该企业内可以被使用的范围，只能被企业自建应用调用。",
        "bizTag": "application"
    },
    {
        "name": "查询用户或部门是否在应用的可用或禁用名单",
        "detail": "该接口用于查询用户、部门、用户组是否在应用的可用或禁用名单中",
        "bizTag": "application"
    },
    {
        "name": "更新应用可用范围",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "启停用应用",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "查询应用管理员列表",
        "detail": "查询审核应用的管理员列表，返回最新10个管理员账户id列表。",
        "bizTag": "contact"
    },
    {
        "name": "获取应用管理员管理范围",
        "detail": "获取应用管理员的管理范围，即该应用管理员能够管理哪些部门。",
        "bizTag": "contact"
    },
    {
        "name": "校验应用管理员",
        "detail": "查询用户是否为应用管理员。",
        "bizTag": "application"
    },
    {
        "name": "查询用户是否在应用开通范围",
        "detail": "当付费套餐是按人数收费 或者 限制最大使用人数时，开放平台会引导企业管理员设置“付费功能开通范围”。  但是受开通范围限制，部分用户就无法使用对应的付费功能。  可以通过此接口，在付费功能点入口判断是否允许某个用户进入使用。",
        "bizTag": "application"
    },
    {
        "name": "查询租户购买的付费方案",
        "detail": "分页查询应用租户下的已付费订单，每次购买对应一个唯一的订单，订单会记录购买的套餐的相关信息，业务方需要自行处理套餐的有效期和付费方案的升级。",
        "bizTag": "application"
    },
    {
        "name": "查询订单详情",
        "detail": "查询某个订单的具体信息。",
        "bizTag": "application"
    },
    {
        "name": "获取多部门应用使用概览",
        "detail": "查看应用在某一天/某一周/某一个月的使用数据，可以根据部门做多层子部门的筛选",
        "bizTag": "application"
    },
    {
        "name": "获取消息推送概览",
        "detail": "目标：查看应用在某一天/某一周/某一个月的机器人消息推送数据，可以根据部门做筛选",
        "bizTag": "application"
    },
    {
        "name": "获取应用使用概览",
        "detail": "查看应用在某一天/某一周/某一个月的使用数据，可以查看租户整体对应用的使用情况，也可以分部门查看。",
        "bizTag": "application"
    },
    {
        "name": "更新应用反馈",
        "detail": "更新应用的反馈数据",
        "bizTag": "application"
    },
    {
        "name": "获取应用反馈列表",
        "detail": "查询应用的反馈数据",
        "bizTag": "application"
    },
    {
        "name": "更新应用红点",
        "detail": "更新应用红点信息，用于工作台场景",
        "bizTag": "application"
    },
    {
        "name": "获取企业席位信息接口",
        "detail": "获取租户下的席位列表，包含席位名称、席位ID、数量及对应有效期。",
        "bizTag": "tenant"
    },
    {
        "name": "获取企业信息",
        "detail": "获取企业名称、企业编号等企业信息",
        "bizTag": "tenant"
    },
    {
        "name": "获取认证信息",
        "detail": "获取企业主体名称、是否认证等信息。",
        "bizTag": "verification_information"
    },
    {
        "name": "创建系统状态",
        "detail": "创建租户维度的系统状态。",
        "bizTag": "personal_settings"
    },
    {
        "name": "删除系统状态",
        "detail": "删除租户维度的系统状态。",
        "bizTag": "personal_settings"
    },
    {
        "name": "修改系统状态",
        "detail": "修改租户维度系统状态。",
        "bizTag": "personal_settings"
    },
    {
        "name": "获取系统状态",
        "detail": "获取租户下所有系统状态。",
        "bizTag": "personal_settings"
    },
    {
        "name": "批量开启系统状态",
        "detail": "批量开启用户系统状态可用。",
        "bizTag": "personal_settings"
    },
    {
        "name": "批量关闭系统状态",
        "detail": "批量关闭用户系统状态可用。",
        "bizTag": "personal_settings"
    },
    {
        "name": "搜索消息",
        "detail": "用户可以通过关键字搜索可见消息，可见性和套件内搜素一致。",
        "bizTag": "search"
    },
    {
        "name": "搜索应用",
        "detail": "用户可以通过关键字搜索到可见应用，应用可见性与套件内搜索一致。",
        "bizTag": "search"
    },
    {
        "name": "创建数据源",
        "detail": "创建一个数据源。",
        "bizTag": "search"
    },
    {
        "name": "删除数据源",
        "detail": "删除一个已存在的数据源。",
        "bizTag": "search"
    },
    {
        "name": "修改数据源",
        "detail": "更新一个已经存在的数据源。",
        "bizTag": "search"
    },
    {
        "name": "获取数据源",
        "detail": "获取已经创建的数据源。",
        "bizTag": "search"
    },
    {
        "name": "批量获取数据源",
        "detail": "批量获取创建的数据源信息。",
        "bizTag": "search"
    },
    {
        "name": "为指定数据项创建索引",
        "detail": "索引一条数据记录。",
        "bizTag": "search"
    },
    {
        "name": "删除数据项",
        "detail": "删除数据项。",
        "bizTag": "search"
    },
    {
        "name": "查询指定数据项",
        "detail": "获取单个数据记录。",
        "bizTag": "search"
    },
    {
        "name": "创建数据范式",
        "detail": "创建一个数据范式。",
        "bizTag": "search"
    },
    {
        "name": "删除数据范式",
        "detail": "删除已存在的数据范式。",
        "bizTag": "search"
    },
    {
        "name": "修改数据范式",
        "detail": "修改数据范式。",
        "bizTag": "search"
    },
    {
        "name": "获取数据范式",
        "detail": "获取单个数据范式。",
        "bizTag": "search"
    },
    {
        "name": "识别文件中的简历信息",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的机动车发票",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的健康证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的港澳居民来往内地通行证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的台湾居民来往大陆通行证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的中国护照",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的银行卡",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的行驶证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的火车票",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的出租车发票",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的身份证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的食品生产许可证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的食品经营许可证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的驾驶证",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的增值税发票",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的营业执照",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "提取文件中的合同字段",
        "detail": "",
        "bizTag": "ai"
    },
    {
        "name": "识别文件中的名片",
        "detail": "名片识别接口，通过上传 JPG / PNG / PDF 等文件类型进行一次性的名片识别。接口适用于20MB以下的文件，适用于英文、日语的名片。",
        "bizTag": "ai"
    },
    {
        "name": "识别图片中的文字",
        "detail": "可识别图片中的文字，按图片中的区域划分，分段返回文本列表。",
        "bizTag": "ai"
    },
    {
        "name": "识别语音文件",
        "detail": "语音文件识别接口，上传整段语音文件进行一次性识别。接口适合 60 秒以内音频识别。",
        "bizTag": "ai"
    },
    {
        "name": "识别流式语音",
        "detail": "语音流式接口，将整个音频文件分片进行传入模型。能够实时返回数据。建议每个音频分片的大小为 100-200ms。",
        "bizTag": "ai"
    },
    {
        "name": "识别文本语种",
        "detail": "机器翻译 (MT)，支持 100 多种语言识别，返回符合 ISO 639-1 标准。",
        "bizTag": "ai"
    },
    {
        "name": "翻译文本",
        "detail": "机器翻译 (MT)，支持以下语种互译：\n\"zh\": 汉语；\n\"zh-Hant\": 繁体汉语；\n\"en\": 英语；\n\"ja\": 日语；\n\"ru\": 俄语；\n\"de\": 德语；\n\"fr\": 法语；\n\"it\": 意大利语；\n\"pl\": 波兰语；\n\"th\": 泰语；\n\"hi\": 印地语；\n\"id\": 印尼语；\n\"es\": 西班牙语；\n\"pt\": 葡萄牙语；\n\"ko\": 朝鲜语；\n\"vi\": 越南语；",
        "bizTag": "ai"
    },
    {
        "name": "查询席位分配详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询席位活跃详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询审计日志列表",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询审计日志详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询数据变更日志列表",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询数据变更日志详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量删除角色成员授权",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量创建角色成员授权",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询角色成员信息",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量删除记录权限用户授权",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量创建记录权限用户授权",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "执行 OQL",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "搜索记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "获取记录详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "编辑记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "删除记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "新建记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量编辑记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询记录列表",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量删除记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "批量新建记录",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "执行函数",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询环境变量列表",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询环境变量详情",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "发起流程",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "同意人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "拒绝人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "转交人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "人工任务加签",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "抄送人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "催办人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "撤销人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "查询人工任务可退回的位置",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "退回人工任务",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "基于人工任务发起群聊",
        "detail": "",
        "bizTag": "app_engine"
    },
    {
        "name": "创建会话",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "更新会话",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "获取会话",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "删除会话",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "发送智能伙伴消息",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "获取智能伙伴消息",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "列出智能伙伴消息",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "创建运行",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "获取运行",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "列出运行",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "取消运行",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "调用技能",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "获取技能信息",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "查询技能列表",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "执行数据知识问答",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "查询数据知识列表",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "获取数据知识分类列表",
        "detail": "",
        "bizTag": "aily"
    },
    {
        "name": "重置用户的企业邮箱密码",
        "detail": "重置用户的企业邮箱密码，仅当用户的邮箱和企业邮箱(别名)一致时生效，可用于处理飞书企业邮箱登录死锁的问题。\n\n邮箱死锁：当用户的登录凭证与飞书企业邮箱一致时，目前飞书登录流程要求用户输入验证码，由于飞书邮箱无单独的帐号体系，则未登录时无法收取邮箱验证码，即陷入死锁。",
        "bizTag": "admin"
    },
    {
        "name": "获取部门维度的用户活跃和功能使用数据",
        "detail": "该接口用于获取部门维度的用户活跃和功能使用数据，即IM（即时通讯）、日历、云文档、音视频会议功能的使用数据。",
        "bizTag": "admin"
    },
    {
        "name": "获取用户维度的用户活跃和功能使用数据",
        "detail": "用于获取用户维度的用户活跃和功能使用数据，即IM（即时通讯）、日历、云文档、音视频会议功能的使用数据。",
        "bizTag": "admin"
    },
    {
        "name": "创建勋章",
        "detail": "使用该接口可以创建一枚完整的勋章信息，一个租户下最多可创建1000枚勋章。",
        "bizTag": "admin"
    },
    {
        "name": "修改勋章信息",
        "detail": "通过该接口可以修改勋章的信息。",
        "bizTag": "admin"
    },
    {
        "name": "上传勋章图片",
        "detail": "通过该接口可以上传勋章详情图、挂饰图的文件，获取对应的文件key。",
        "bizTag": "admin"
    },
    {
        "name": "获取勋章列表",
        "detail": "可以通过该接口列出租户下所有的勋章，勋章的排列顺序是按照创建时间倒序排列。",
        "bizTag": "admin"
    },
    {
        "name": "获取勋章详情",
        "detail": "可以通过该接口查询勋章的详情。",
        "bizTag": "admin"
    },
    {
        "name": "创建授予名单",
        "detail": "通过该接口可以为特定勋章创建一份授予名单，一枚勋章下最多可创建1000份授予名单。",
        "bizTag": "admin"
    },
    {
        "name": "删除授予名单",
        "detail": "通过该接口可以删除特定授予名单的信息。",
        "bizTag": "admin"
    },
    {
        "name": "修改授予名单",
        "detail": "通过该接口可以修改特定授予名单的相关信息。",
        "bizTag": "admin"
    },
    {
        "name": "获取授予名单列表",
        "detail": "通过该接口可以获取特定勋章下的授予名单列表，授予名单的排列顺序按照创建时间倒序排列。",
        "bizTag": "admin"
    },
    {
        "name": "获取授予名单详情",
        "detail": "通过该接口可以获取特定授予名单的信息。",
        "bizTag": "admin"
    },
    {
        "name": "查询帖子信息",
        "detail": "",
        "bizTag": "moments"
    },
    {
        "name": "批量获取员工花名册信息",
        "detail": "根据员工飞书用户 ID / 员工状态 / 雇员类型等搜索条件 ，批量获取员工花名册字段信息。字段包括「系统标准字段 / system_fields」和「自定义字段 / custom_fields」。",
        "bizTag": "ehr"
    },
    {
        "name": "下载人员的附件",
        "detail": "根据文件 token 下载文件。\n\n调用 「批量获取员工花名册信息」接口的返回值中，「文件」类型的字段 id，即是文件 token",
        "bizTag": "ehr"
    },
    {
        "name": "获取飞书人事对象列表",
        "detail": "获取「飞书人事」中的对象列表，含系统预置对象与自定义对象。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取自定义字段列表",
        "detail": "获取「飞书人事」具体对象下的自定义字段列表。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取字段详情",
        "detail": "获取「飞书人事」具体对象下某自定义字段的详细信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "增加字段枚举值选项",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "修改字段枚举值选项",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询枚举信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询国家/地区信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询省份/主要行政区信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询城市信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询区/县信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询国籍信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建国家证件类型",
        "detail": "创建国家证件类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除国家证件类型",
        "detail": "删除国家证件类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新国家证件类型",
        "detail": "更新国家证件类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个国家证件类型",
        "detail": "根据 ID 查询单个国家证件类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询国家证件类型",
        "detail": "批量查询国家证件类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询银行信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询支行信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询货币信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询时区信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询语言信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建人员类型",
        "detail": "创建人员类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除人员类型",
        "detail": "删除人员类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新人员类型",
        "detail": "更新人员类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个人员类型",
        "detail": "根据 ID 查询单个人员类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询人员类型",
        "detail": "批量查询人员类型。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建工时制度",
        "detail": "创建工时制度。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除工时制度",
        "detail": "删除工时制度。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新工时制度",
        "detail": "更新工时制度。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个工时制度",
        "detail": "根据 ID 查询单个工时制度。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询工时制度",
        "detail": "批量查询工时制度。",
        "bizTag": "feishu_people"
    },
    {
        "name": "ID 转换",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询员工信息",
        "detail": "接口描述",
        "bizTag": "corehr"
    },
    {
        "name": "搜索员工信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "添加人员",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建个人信息",
        "detail": "创建个人信息",
        "bizTag": "corehr"
    },
    {
        "name": "更新个人信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除个人信息",
        "detail": "删除人员的个人信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "上传文件",
        "detail": "上传文件。",
        "bizTag": "feishu_people"
    },
    {
        "name": "下载文件",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建雇佣信息",
        "detail": "创建人员的雇佣信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新雇佣信息",
        "detail": "更新雇佣信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除雇佣信息",
        "detail": "删除人员的雇佣信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建任职信息",
        "detail": "在系统中第一次创建员工任职数据，通常在员工入职或者做数据批量导入的时候使用，【任职原因】只支持填写“入职”。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除任职信息",
        "detail": "删除人员的任职信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新任职信息",
        "detail": "更新任职信息，「任职原因」不可填「onboarding」",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取任职信息列表",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询员工任职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询任职信息",
        "detail": "批量查询人员的任职信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个任职信息",
        "detail": "根据 ID 查询单任职信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建兼职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "更新兼职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除兼职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询兼职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询部门操作日志",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建部门",
        "detail": "创建部门。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新部门",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取父部门信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询部门",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询指定时间范围内当前生效信息发生变更的部门",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询指定生效日期的部门基本信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询指定生效日期的部门架构树",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询部门版本信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "搜索部门信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除部门 V2",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建地点",
        "detail": "创建地点。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新地点",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询单个地点",
        "detail": "根据 ID 查询单个地点。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询当前生效信息发生变更的地点",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "通过地点 ID 批量获取地点信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量分页查询地点信息",
        "detail": "批量查询地点。",
        "bizTag": "feishu_people"
    },
    {
        "name": "启用/停用地点",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除地点",
        "detail": "删除地点。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除地点地址",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "更新地点地址",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "添加地点地址",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建公司",
        "detail": "创建公司。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新公司",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "启用/停用公司",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询单个公司",
        "detail": "根据 ID 查询单个公司。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询公司",
        "detail": "批量查询公司。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询指定时间范围内当前生效信息发生变更的公司",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "通过公司 ID 批量获取公司信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除公司",
        "detail": "删除公司。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建成本中心",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "启用 / 停用成本中心",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询当前生效信息发生变更的成本中心",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "搜索成本中心信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除成本中心",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建成本中心版本",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "更正成本中心版本",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销成本中心版本",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "根据流程 ID 查询组织架构调整记录",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询部门调整内容",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询人员调整内容",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建序列",
        "detail": "创建职务序列。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新序列",
        "detail": "更新职务序列。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个序列",
        "detail": "根据 ID 查询单个职务序列。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询序列",
        "detail": "批量查询职务序列。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询当前生效信息发生变更的序列",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "通过序列 ID 批量获取序列信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除序列",
        "detail": "删除职务序列。",
        "bizTag": "feishu_people"
    },
    {
        "name": "新建职级",
        "detail": "创建职务级别。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新单个职级",
        "detail": "更新职务级别。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个职级",
        "detail": "根据 ID 查询单个职务级别。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询职级",
        "detail": "批量查询职务级别。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询当前生效信息发生变更的职级",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "通过职级 ID 批量获取职级信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除职级",
        "detail": "删除职务级别。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建职等",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "更新职等",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询职等",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询当前生效信息发生变更的职等",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除职等",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建职务",
        "detail": "创建职务。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除职务",
        "detail": "删除职务。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新职务",
        "detail": "更新职务。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个职务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询职务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销入职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "恢复入职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "直接创建待入职",
        "detail": "创建待入职人员。",
        "bizTag": "corehr"
    },
    {
        "name": "更新待入职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除待入职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询待入职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询单个待入职信息",
        "detail": "根据 ID 查询单个待入职人员。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询待入职信息",
        "detail": "批量查询待入职人员。",
        "bizTag": "feishu_people"
    },
    {
        "name": "搜索待入职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "流转入职任务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "操作员工完成入职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除待入职（不推荐）",
        "detail": "删除待入职人员。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新待入职信息（不推荐）",
        "detail": "更新待入职信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "新增试用期考核信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "启用/停用试用期考核功能",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "更新试用期考核信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "搜索试用期信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "删除试用期考核信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "发起转正",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销转正",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "发起员工异动",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取异动类型列表",
        "detail": "获取异动类型列表。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取异动原因列表",
        "detail": "获取异动原因列表。",
        "bizTag": "feishu_people"
    },
    {
        "name": "搜索员工异动信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销异动",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "发起员工异动(不推荐)",
        "detail": "创建员工异动信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询员工离职原因列表",
        "detail": "查询「飞书人事」-「离职设置」中的离职原因。",
        "bizTag": "feishu_people"
    },
    {
        "name": "操作员工离职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "编辑离职信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销离职",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "搜索离职信息",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "新建合同",
        "detail": "创建合同。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新合同",
        "detail": "更新合同。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除合同",
        "detail": "删除合同。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个合同",
        "detail": "根据 ID 查询单个合同。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询合同",
        "detail": "批量查询合同。",
        "bizTag": "feishu_people"
    },
    {
        "name": "搜索合同",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量创建/更新明细行",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量删除明细行",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量创建/更新填报行",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量删除填报行",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询编制规划方案",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询编制规划明细信息",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "创建假期发放记录",
        "detail": "向飞书人事休假系统写入假期授予记录。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除假期发放记录",
        "detail": "删除飞书人事休假系统中的假期授予记录（仅支持删除授予来源是「手动授予」或「外部系统授予」的记录）。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取假期类型列表",
        "detail": "获取休假设置后台配置的假期类型列表（比如年假、事假、婚假等）。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询员工假期余额",
        "detail": "批量获取员工各个假期的余额数据。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询员工请假记录",
        "detail": "批量获取员工的请假记录数据。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取工作日历",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "根据适用条件获取工作日历 ID",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取工作日历日期详情",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询用户授权",
        "detail": "批量查询「飞书人事」-「权限设置」中的用户授权信息",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个用户授权",
        "detail": "查询单个用户授权",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量获取角色列表",
        "detail": "批量查询「飞书人事」-「权限设置」-「角色设置」中的角色列表。",
        "bizTag": "feishu_people"
    },
    {
        "name": "为用户授权角色",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新用户被授权的数据范围",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "移除用户被授权的角色",
        "detail": "",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询员工 HRBP / 属地 BP",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询部门 HRBP",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "查询部门 / 地点的 HRBP / 属地 BP",
        "detail": "通过部门或工作地点，查询对应的 HRBP/属地 BP。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取 HRBP 列表",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取组织类角色授权列表",
        "detail": "查询组织类角色的授权信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询流程实例列表",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取单个流程详情",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取流程表单数据",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤销流程",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "撤回流程",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "获取指定人员审批任务列表",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "通过/拒绝审批任务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "加签审批任务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "转交审批任务",
        "detail": "",
        "bizTag": "corehr"
    },
    {
        "name": "批量查询员工薪资档案",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "批量查询薪资项",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "批量查询薪资统计指标",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "批量获取薪资项分类信息",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "获取员工薪资标准",
        "detail": "根据员工获取匹配的薪资标准信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询薪资方案",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "批量查询定调薪原因",
        "detail": "",
        "bizTag": "compensation_management"
    },
    {
        "name": "批量查询算薪项",
        "detail": "",
        "bizTag": "payroll"
    },
    {
        "name": "查询成本分摊报表汇总数据",
        "detail": "",
        "bizTag": "payroll"
    },
    {
        "name": "批量查询成本分摊方案",
        "detail": "",
        "bizTag": "payroll"
    },
    {
        "name": "获取薪资组基本信息",
        "detail": "",
        "bizTag": "payroll"
    },
    {
        "name": "查询地点列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取地址列表",
        "detail": "获取地址列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取角色详情",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取角色列表",
        "detail": "获取角色列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取用户角色列表",
        "detail": "获取用户角色列表。",
        "bizTag": "hire"
    },
    {
        "name": "新建职位",
        "detail": "新建职位，字段的是否必填，以系统中的「职位字段管理」中的设置为准。",
        "bizTag": "hire"
    },
    {
        "name": "更新职位",
        "detail": "更新职位信息，该接口为全量更新，若字段没有返回值，则原有值将会被清空。字段的是否必填，将以系统中的「职位字段管理」中的设置为准。",
        "bizTag": "hire"
    },
    {
        "name": "更新职位设置",
        "detail": "更新职位设置，包括面试评价表、Offer 申请表等。接口将按照所选择的「更新选项」进行设置参数校验和更新。",
        "bizTag": "hire"
    },
    {
        "name": "更新职位相关人员",
        "detail": "更新职位相关人员。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位详情",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取职位信息",
        "detail": "根据职位 ID 获取职位信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位上的招聘人员信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取职位设置",
        "detail": "获取职位设置。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位列表",
        "detail": "根据更新时间获取职位列表，仅支持获取默认字段信息，获取详细信息可调用[获取职位信息](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/job/get)接口。",
        "bizTag": "hire"
    },
    {
        "name": "关闭职位",
        "detail": "支持关闭职位，关闭后，职位将同步从官网、内推、猎头渠道下线。",
        "bizTag": "hire"
    },
    {
        "name": "重启职位",
        "detail": "支持开启职位。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位模板",
        "detail": "获取社招、校招职位模板中的职位字段，包括系统默认字段和自定义字段。",
        "bizTag": "hire"
    },
    {
        "name": "发布职位广告",
        "detail": "支持把职位发布至招聘官网、内推平台。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位广告发布记录",
        "detail": "获取职位广告发布记录。",
        "bizTag": "hire"
    },
    {
        "name": "获取职能分类列表",
        "detail": "获取职能分类列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位类别列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建招聘需求",
        "detail": "创建招聘需求，除招聘需求编号为必填外，其他字段是否必填与飞书招聘「招聘需求字段管理」内设置一致。",
        "bizTag": "hire"
    },
    {
        "name": "更新招聘需求",
        "detail": "更新招聘需求。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘需求信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘需求列表",
        "detail": "获取招聘需求列表。",
        "bizTag": "hire"
    },
    {
        "name": "删除招聘需求",
        "detail": "删除招聘需求。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘需求模板列表",
        "detail": "获取招聘需求模板。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘流程信息",
        "detail": "获取全部招聘流程信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取项目列表",
        "detail": "获取项目列表（概念上一批集体启动和管理的职位可以定义为一个项目，例如 「2012 秋招项目」）。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才标签信息列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取信息登记表列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取面试评价表列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取面试轮次类型列表",
        "detail": "获取面试轮次类型列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取面试登记表列表",
        "detail": "获取面试登记表模板列表。",
        "bizTag": "hire"
    },
    {
        "name": "查询面试官信息列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新面试官信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新 Offer 申请表自定义字段",
        "detail": "- 本文档支持通过接口更新「飞书招聘」-「设置」-「Offer 申请表设置」中 Offer 申请表的自定义字段配置；\n- 当前修改申请表信息（包括更新自定义字段）后，所有申请表的 schema_id 均会更新，即所有申请表均会新增一个版本，申请表的 schema_id 会在创建 offer、更新 offer 中使用；\n- 「飞书招聘」中 Offer 申请表自定义字段创建后，不支持修改字段类型，本接口亦不支持更新字段类型；\n- 当前字段类型为「公式」的，不支持通过接口更新。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 申请表信息",
        "detail": "获取 Offer 申请表模板信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 申请表列表",
        "detail": "获取 Offer 申请表列表。",
        "bizTag": "hire"
    },
    {
        "name": "查询人才内推信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取内推官网下职位广告列表",
        "detail": "获取内推官网下的职位列表。自定义数据暂不支持列表获取，请从「获取内推官网下职位广告详情」接口获取。",
        "bizTag": "hire"
    },
    {
        "name": "获取内推官网下职位广告详情",
        "detail": "根据广告 ID 获取内推官网下的职位广告详情。",
        "bizTag": "hire"
    },
    {
        "name": "获取内推信息",
        "detail": "根据投递 ID 获取内推信息。",
        "bizTag": "hire"
    },
    {
        "name": "新建招聘官网推广渠道",
        "detail": "根据招聘官网 ID 和推广渠道名称创建招聘官网推广渠道。",
        "bizTag": "hire"
    },
    {
        "name": "删除招聘官网推广渠道",
        "detail": "根据招聘官网 ID 和推广渠道 ID 删除招聘官网推广渠道。",
        "bizTag": "hire"
    },
    {
        "name": "更新招聘官网推广渠道",
        "detail": "根据招聘官网 ID 和推广渠道 ID 更改推广渠道名称。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘官网推广渠道列表",
        "detail": "根据官网 ID 分页获取推广渠道列表。",
        "bizTag": "hire"
    },
    {
        "name": "新建招聘官网用户",
        "detail": "新建招聘官网用户。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘官网下职位广告详情",
        "detail": "获取招聘官网下职位广告详情。",
        "bizTag": "hire"
    },
    {
        "name": "搜索招聘官网下的职位广告列表",
        "detail": "搜索招聘官网下的职位列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘官网下的职位广告列表",
        "detail": "获取招聘官网下的职位列表。自定义数据暂不支持列表获取，请从「获取招聘官网下职位广告详情」接口获取。",
        "bizTag": "hire"
    },
    {
        "name": "新建招聘官网投递",
        "detail": "新建招聘官网投递。",
        "bizTag": "hire"
    },
    {
        "name": "根据简历附件创建招聘官网投递任务",
        "detail": "根据简历附件解析创建招聘官网投递。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘官网投递任务结果",
        "detail": "获取招聘官网投递任务信息，如果获取到的数据data为空，仍然继续轮询，直到data不为空时，再查询data里面的数据。",
        "bizTag": "hire"
    },
    {
        "name": "获取招聘官网列表",
        "detail": "获取招聘官网列表。",
        "bizTag": "hire"
    },
    {
        "name": "设置猎头保护期",
        "detail": "设置猎头保护期。",
        "bizTag": "hire"
    },
    {
        "name": "获取猎头供应商信息",
        "detail": "根据猎头供应商 ID 获取猎头供应商信息。",
        "bizTag": "hire"
    },
    {
        "name": "查询猎头保护期信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询猎头供应商信息",
        "detail": "根据猎头供应商名称查询猎头供应商信息。",
        "bizTag": "hire"
    },
    {
        "name": "查询猎头供应商下猎头列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "搜索猎头供应商列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "禁用/取消禁用猎头",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建人才外部信息",
        "detail": "创建人才外部信息。",
        "bizTag": "hire"
    },
    {
        "name": "更新人才外部信息",
        "detail": "更新人才外部信息。",
        "bizTag": "hire"
    },
    {
        "name": "创建外部投递",
        "detail": "导入来自其他系统的投递信息，创建为外部投递。",
        "bizTag": "hire"
    },
    {
        "name": "更新外部投递",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询外部投递列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除外部投递",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建外部面试",
        "detail": "导入来自其他系统的面试信息，创建为外部面试。",
        "bizTag": "hire"
    },
    {
        "name": "更新外部面试",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询外部面试列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除外部面试",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建外部面评",
        "detail": "导入来自其他系统的面评信息，创建为外部面评。",
        "bizTag": "hire"
    },
    {
        "name": "更新外部面评",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建外部 Offer",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新外部 Offer",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询外部 Offer 列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除外部 Offer",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建外部背调",
        "detail": "导入来自其他系统的背调信息，创建为外部背调。",
        "bizTag": "hire"
    },
    {
        "name": "更新外部背调",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询外部背调列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除外部背调",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "导入外部内推奖励",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除外部内推奖励",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "批量加入/移除人才库中人才",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取人才库列表",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "将人才加入人才库",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "操作人才标签",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建人才",
        "detail": "用于在企业内创建一个人才。姓名为系统预设的必填字段，邮箱/电话字段请在飞书招聘标准简历模板设置中确认是否必填。可配合[获取人才字段](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query)接口获取自定义字段信息。",
        "bizTag": "hire"
    },
    {
        "name": "更新人才",
        "detail": "用于在企业内更新一个人才。姓名为系统预设的必填字段，邮箱/电话字段请在飞书招聘标准简历模板设置中确认是否必填。可配合[获取人才字段](/ssl:ttdoc/ukTMukTMukTM/uMzM1YjLzMTN24yMzUjN/hire-v1/talent_object/query)接口获取自定义字段信息。",
        "bizTag": "hire"
    },
    {
        "name": "将人才加入指定文件夹",
        "detail": "将人才加入指定文件夹。",
        "bizTag": "hire"
    },
    {
        "name": "将人才从指定文件夹移除",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取人才文件夹列表",
        "detail": "用于获取招聘系统中人才文件夹信息。",
        "bizTag": "hire"
    },
    {
        "name": "批量获取人才ID",
        "detail": "通过手机号或邮箱获取人才 ID。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才列表",
        "detail": "根据更新时间获取人才列表，仅支持获取默认字段信息，获取详细信息可调用「获取人才详细」接口。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才字段",
        "detail": "获取人才字段。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才信息",
        "detail": "根据人才 ID 获取人才信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才详情",
        "detail": "根据人才 ID 获取人才信息。",
        "bizTag": "hire"
    },
    {
        "name": "更新人才在职状态",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "加入/移除屏蔽名单",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取投递详情",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "恢复投递",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建投递",
        "detail": "根据人才 ID 和职位 ID 创建投递。",
        "bizTag": "hire"
    },
    {
        "name": "终止投递",
        "detail": "根据投递 ID 修改投递状态为「已终止」。",
        "bizTag": "hire"
    },
    {
        "name": "转移投递阶段",
        "detail": "转移投递阶段。",
        "bizTag": "hire"
    },
    {
        "name": "获取终止投递原因",
        "detail": "获取终止投递原因。",
        "bizTag": "hire"
    },
    {
        "name": "获取投递信息",
        "detail": "根据投递 ID 获取单个投递信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取投递列表",
        "detail": "根据限定条件获取投递列表信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取申请表附加信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取简历评估信息列表",
        "detail": "获取简历评估信息。",
        "bizTag": "hire"
    },
    {
        "name": "添加笔试结果",
        "detail": "根据投递 ID 添加该投递下的笔试结果。",
        "bizTag": "hire"
    },
    {
        "name": "获取笔试列表",
        "detail": "批量获取人才在某投递流程中的笔试信息，如作答状态、笔试得分等。（目前仅支持获取 1w 条数据，若数据量较大，可通过控制 test_start_time 查询条件分批次获取全量数据）。",
        "bizTag": "hire"
    },
    {
        "name": "获取面试信息",
        "detail": "根据投递 ID 或面试时间获取面试信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取人才面试信息",
        "detail": "获取人才面试信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取面试评价详细信息",
        "detail": "获取面试评价详细信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取面试评价详细信息（新版）",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "批量获取面试评价详细信息",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "批量获取面试评价详细信息（新版）",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取面试记录附件",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取面试速记明细",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取面试满意度问卷列表",
        "detail": "获取面试满意度问卷列表。",
        "bizTag": "hire"
    },
    {
        "name": "创建 Offer",
        "detail": "创建 Offer 时，需传入本文档中标注为必传的参数，其余参数是否必传参考「获取 Offer 申请表模板信息」的参数定义。",
        "bizTag": "hire"
    },
    {
        "name": "更新 Offer 信息",
        "detail": "1. 更新 Offer 时，需传入本文档中标注为必传的参数，其余参数是否必传参考「获取 Offer 申请表模板信息」的参数定义；\n2. 对系统中已存在的 offer 进行更新的，若更新 offer 中含有「修改需审批」的字段，更新后原 Offer 的审批会自动撤回，需要重新发起审批。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 信息",
        "detail": "根据投递 ID 获取 Offer 信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 详情",
        "detail": "根据 Offer ID 获取 Offer 详细信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 列表",
        "detail": "根据人才 ID 获取 Offer 列表。",
        "bizTag": "hire"
    },
    {
        "name": "更新 Offer 状态",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新实习 Offer 入/离职状态",
        "detail": "对「实习待入职」状态的实习 Offer 确认入职、放弃入职，或对「实习已入职」状态的实习 Offer 操作离职。",
        "bizTag": "hire"
    },
    {
        "name": "获取背调信息列表",
        "detail": "根据投递 ID 或背调更新时间获取背调信息。",
        "bizTag": "hire"
    },
    {
        "name": "创建三方协议",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取三方协议",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新三方协议",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "删除三方协议",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "更新 e-HR 导入任务结果",
        "detail": "在处理完导入 e-HR 事件后，可调用该接口，更新  e-HR 导入任务结果。",
        "bizTag": "hire"
    },
    {
        "name": "操作候选人入职",
        "detail": "根据投递 ID 操作候选人入职并创建员工。投递须处于「待入职」阶段，可通过「转移阶段」接口变更投递状态。",
        "bizTag": "hire"
    },
    {
        "name": "更新员工状态",
        "detail": "根据员工 ID 更新员工转正、离职状态。",
        "bizTag": "hire"
    },
    {
        "name": "通过投递 ID 获取入职信息",
        "detail": "通过投递 ID 获取入职信息。",
        "bizTag": "hire"
    },
    {
        "name": "通过员工 ID 获取入职信息",
        "detail": "通过员工 ID 获取入职信息。",
        "bizTag": "hire"
    },
    {
        "name": "批量获取待办事项",
        "detail": "获取待办列表。",
        "bizTag": "hire"
    },
    {
        "name": "获取简历评估任务列表",
        "detail": "获取员工评估任务。",
        "bizTag": "hire"
    },
    {
        "name": "获取笔试阅卷任务列表",
        "detail": "获取员工笔试阅卷任务。",
        "bizTag": "hire"
    },
    {
        "name": "获取面试任务列表",
        "detail": "获取员工面试任务。",
        "bizTag": "hire"
    },
    {
        "name": "创建备注",
        "detail": "创建备注信息。",
        "bizTag": "hire"
    },
    {
        "name": "更新备注",
        "detail": "根据备注 ID 更新备注信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取备注",
        "detail": "根据备注 ID 获取备注信息。",
        "bizTag": "hire"
    },
    {
        "name": "获取备注列表",
        "detail": "获取备注列表。",
        "bizTag": "hire"
    },
    {
        "name": "删除备注",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "获取简历来源列表",
        "detail": "获取简历来源列表。",
        "bizTag": "hire"
    },
    {
        "name": "创建账号自定义字段",
        "detail": "定制用户在服务商处的身份标示字段（如用户在服务商处的租户 ID）。用户在飞书招聘后台添加帐号后，系统会推送「帐号绑定」事件给开发者，事件将携带用户填写的自定义字段信息，开发者可根据此信息识别飞书招聘用户在服务商处的身份信息，完成飞书招聘用户和服务商帐号的绑定，并以此来推送对应的套餐或试卷列表等。",
        "bizTag": "hire"
    },
    {
        "name": "更新账号自定义字段",
        "detail": "更新用户在服务商处的身份标示字段（如用户在服务商处的租户 ID），此方法只会更新同一 scope 内 key 一致的自定义字段。",
        "bizTag": "hire"
    },
    {
        "name": "删除账号自定义字段",
        "detail": "删除用户在服务商处的身份标示字段（如用户在服务商处的租户 ID）。删除后，不影响已添加帐号对应的自定义字段的值。但在添加新帐号时，将不能再使用此自定义字段。删除不支持撤销，对应的 key 将无法再次复用。",
        "bizTag": "hire"
    },
    {
        "name": "创建背调自定义字段",
        "detail": "定制用户在发起背调时的自定义字段。",
        "bizTag": "hire"
    },
    {
        "name": "更新背调自定义字段",
        "detail": "更新用户在发起背调时的自定义字段。更新操作不支持更新自定义字段类型，且将影响已发起的背调表单展示。",
        "bizTag": "hire"
    },
    {
        "name": "删除背调自定义字段",
        "detail": "删除用户在发起背调时的自定义字段，删除不影响已创建的背调，删除后对应的自定义字段的 key 不能再复用。",
        "bizTag": "hire"
    },
    {
        "name": "创建背调套餐和附加调查项",
        "detail": "定制指定帐号可用的背调套餐和附加调查项信息。",
        "bizTag": "hire"
    },
    {
        "name": "更新背调套餐和附加调查项",
        "detail": "更新指定帐号可用的背调套餐和附加调查项信息，更新将影响已发起背调的表单项展示。",
        "bizTag": "hire"
    },
    {
        "name": "删除背调套餐和附加调查项",
        "detail": "删除指定帐号的指定背调套餐和附加调查项信息，删除不会影响已创建的背调。",
        "bizTag": "hire"
    },
    {
        "name": "更新背调订单进度",
        "detail": "更新指定背调的进度信息。",
        "bizTag": "hire"
    },
    {
        "name": "回传背调订单的最终结果",
        "detail": "回传背调订单的最终结果。",
        "bizTag": "hire"
    },
    {
        "name": "终止背调订单",
        "detail": "终止背调订单。",
        "bizTag": "hire"
    },
    {
        "name": "创建试卷列表",
        "detail": "推送试卷列表。",
        "bizTag": "hire"
    },
    {
        "name": "更新试卷列表",
        "detail": "更新试卷。",
        "bizTag": "hire"
    },
    {
        "name": "删除试卷列表",
        "detail": "删除试卷。",
        "bizTag": "hire"
    },
    {
        "name": "回传笔试安排结果",
        "detail": "回传笔试安排结果",
        "bizTag": "hire"
    },
    {
        "name": "回传笔试结果",
        "detail": "回传笔试结果",
        "bizTag": "hire"
    },
    {
        "name": "启用内推账户",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "查询内推账户",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "注册内推账户",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "停用内推账户",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "全额提取内推账户余额",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "内推账户提现数据对账",
        "detail": "",
        "bizTag": "hire"
    },
    {
        "name": "创建附件",
        "detail": "上传附件文件。",
        "bizTag": "hire"
    },
    {
        "name": "获取附件信息",
        "detail": "获取招聘系统中附件的元信息，比如文件名、创建时间、文件 URL 等。",
        "bizTag": "hire"
    },
    {
        "name": "获取附件 PDF 格式下载链接",
        "detail": "根据附件 ID 获取附件预览信息。",
        "bizTag": "hire"
    },
    {
        "name": "创建 OKR 周期",
        "detail": "根据周期规则创建一个 OKR 周期。",
        "bizTag": "okr"
    },
    {
        "name": "修改 OKR 周期状态",
        "detail": "修改某个 OKR 周期的状态为「正常」、「失效」或「隐藏」，对租户所有人生效，请谨慎操作",
        "bizTag": "okr"
    },
    {
        "name": "获取 OKR 周期列表",
        "detail": "获取 OKR 周期列表。",
        "bizTag": "okr"
    },
    {
        "name": "获取 OKR 周期规则",
        "detail": "获取租户的周期规则列表。",
        "bizTag": "okr"
    },
    {
        "name": "获取用户的 OKR 列表",
        "detail": "根据用户的 id 获取 OKR 列表。",
        "bizTag": "okr"
    },
    {
        "name": "批量获取 OKR",
        "detail": "根据 OKR id 批量获取 OKR。",
        "bizTag": "okr"
    },
    {
        "name": "创建 OKR 进展记录",
        "detail": "创建 OKR 进展记录。",
        "bizTag": "okr"
    },
    {
        "name": "删除 OKR 进展记录",
        "detail": "根据 ID 删除 OKR 进展记录。",
        "bizTag": "okr"
    },
    {
        "name": "更新 OKR 进展记录",
        "detail": "根据 OKR 进展记录 ID 更新进展详情。",
        "bizTag": "okr"
    },
    {
        "name": "获取 OKR 进展记录",
        "detail": "根据 ID 获取 OKR 进展记录详情。",
        "bizTag": "okr"
    },
    {
        "name": "上传进展记录图片",
        "detail": "上传进展记录图片。",
        "bizTag": "okr"
    },
    {
        "name": "查询复盘信息",
        "detail": "根据周期和用户查询复盘信息。",
        "bizTag": "okr"
    },
    {
        "name": "录入身份信息",
        "detail": "该接口用于录入实名认证的身份信息，在唤起有源活体认证前，需要使用该接口进行实名认证。",
        "bizTag": "human_authentication"
    },
    {
        "name": "上传人脸基准图片",
        "detail": "无源人脸比对流程，开发者后台通过调用此接口将基准图片上传到飞书后台，做检测时的对比使用。",
        "bizTag": "human_authentication"
    },
    {
        "name": "裁剪人脸图片",
        "detail": "无源人脸比对流程，开发者后台通过调用此接口对基准图片做规范校验及处理。",
        "bizTag": "human_authentication"
    },
    {
        "name": "查询人脸认证结果",
        "detail": "无源人脸比对流程，开发者后台通过调用此接口请求飞书后台，对本次活体比对结果做校验。",
        "bizTag": "human_authentication"
    },
    {
        "name": "修改用户部分信息",
        "detail": "飞书智能门禁在人脸识别成功后会有韦根信号输出，输出用户的卡号。\n对于使用韦根协议的门禁系统，企业可使用该接口录入用户卡号。",
        "bizTag": "acs"
    },
    {
        "name": "获取单个用户信息",
        "detail": "该接口用于获取智能门禁中单个用户的信息。",
        "bizTag": "acs"
    },
    {
        "name": "获取用户列表",
        "detail": "使用该接口获取智能门禁中所有用户信息。",
        "bizTag": "acs"
    },
    {
        "name": "上传人脸图片",
        "detail": "用户需要录入人脸图片才可以使用门禁考勤机。使用该 API 上传门禁用户的人脸图片。",
        "bizTag": "acs"
    },
    {
        "name": "下载人脸图片",
        "detail": "对于已经录入人脸图片的用户，可以使用该接口下载用户人脸图片。",
        "bizTag": "acs"
    },
    {
        "name": "设备绑定权限组",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "获取权限组信息",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "删除权限组",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "创建或更新权限组",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "删除访客",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "添加访客",
        "detail": "",
        "bizTag": "acs"
    },
    {
        "name": "获取门禁设备列表",
        "detail": "使用该接口获取租户内所有门禁设备。",
        "bizTag": "acs"
    },
    {
        "name": "获取门禁记录列表",
        "detail": "用户在门禁考勤机上成功开门或打卡后，智能门禁应用都会生成一条门禁记录。\n\n该接口返回满足查询参数的识别记录。",
        "bizTag": "acs"
    },
    {
        "name": "下载开门时的人脸识别图片",
        "detail": "用户在门禁考勤机上成功开门或打卡后，智能门禁应用都会生成一条门禁记录，对于使用人脸识别方式进行开门的识别记录，还会有抓拍图。\n\n可以用该接口下载开门时的人脸识别照片。",
        "bizTag": "acs"
    },
    {
        "name": "获取周期列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取项目列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "批量查询补充信息",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "批量导入补充信息",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "批量删除补充信息",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "更新人员组成员",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取被评估人信息",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取评估模板配置",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取评估项列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取标签填写题配置",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取指标列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取指标模板列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取指标字段列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取指标标签列表",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取周期任务（指定用户）",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取周期任务（全部用户）",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取被评估人关键指标结果",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "录入被评估人关键指标数据",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "获取绩效结果",
        "detail": "获取绩效结果",
        "bizTag": "performance"
    },
    {
        "name": "获取绩效详情数据",
        "detail": "",
        "bizTag": "performance"
    },
    {
        "name": "创建草稿",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "更新草稿",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "创建免审词条",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "更新免审词条",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "删除免审词条",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "获取词条详情",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "获取词条列表",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "精准搜索词条",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "模糊搜索词条",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "词条高亮",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "获取词典分类",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "获取词库列表",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "上传图片",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "下载图片",
        "detail": "",
        "bizTag": "baike"
    },
    {
        "name": "获取OpenAPI审计日志数据",
        "detail": "",
        "bizTag": "security_and_compliance"
    },
    {
        "name": "获取行为审计日志数据",
        "detail": "获取行为审计日志数据",
        "bizTag": "admin"
    },
    {
        "name": "获取妙记统计数据",
        "detail": "通过这个接口，可以获得妙记的访问情况统计，包含PV、UV、访问过的 user id、访问过的 user timestamp。",
        "bizTag": "minutes"
    },
    {
        "name": "获取妙记信息",
        "detail": "通过这个接口，可以得到一篇妙记的基础概述信息，包含 `owner_id`、`create_time`、标题、封面、时长和 URL。",
        "bizTag": "minutes"
    },
    {
        "name": "获取工作台访问数据",
        "detail": "",
        "bizTag": "workplace"
    },
    {
        "name": "获取定制工作台访问数据",
        "detail": "",
        "bizTag": "workplace"
    },
    {
        "name": "获取定制工作台小组件访问数据",
        "detail": "",
        "bizTag": "workplace"
    },
    {
        "name": "获取用户自定义常用的应用",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取管理员推荐的应用",
        "detail": "",
        "bizTag": "application"
    },
    {
        "name": "获取当前设置的推荐规则列表",
        "detail": "获取当前设置的推荐规则列表。",
        "bizTag": "application"
    },
    {
        "name": "用户数据维度绑定",
        "detail": "通过该接口，可为指定应用下的用户绑定一类数据维度，支持批量给多个用户同时增量授权。",
        "bizTag": "mdm"
    },
    {
        "name": "用户数据维度解绑",
        "detail": "通过该接口，可为指定应用下的指定用户解除一类数据维度。",
        "bizTag": "mdm"
    },
    {
        "name": "查询规则",
        "detail": "查询规则。",
        "bizTag": "report"
    },
    {
        "name": "移除规则看板",
        "detail": "移除规则看板",
        "bizTag": "report"
    },
    {
        "name": "查询任务",
        "detail": "查询任务。",
        "bizTag": "report"
    },
    {
        "name": "创建任务",
        "detail": "该接口可以创建一个任务，支持填写任务的基本信息，包括任务的标题，描述及协作者等。\n在此基础上，创建任务时可以设置截止时间和重复规则，将任务设置为定期执行的重复任务。通过添加协作者，则可以让其他用户协同完成该任务。\n此外，接口也提供了一些支持自定义内容的字段，调用方可以实现定制化效果，如完成任务后跳转到指定结束界面。",
        "bizTag": "task"
    },
    {
        "name": "删除任务",
        "detail": "该接口用于删除任务。",
        "bizTag": "task"
    },
    {
        "name": "更新任务",
        "detail": "该接口用于修改任务的标题、描述、时间、来源等相关信息。",
        "bizTag": "task"
    },
    {
        "name": "完成任务",
        "detail": "该接口用于将任务状态修改为“已完成”。\n完成任务是指整个任务全部完成，而不支持执行者分别完成任务，执行成功后，任务对所有关联用户都变为完成状态。",
        "bizTag": "task"
    },
    {
        "name": "取消完成任务",
        "detail": "该接口用于取消任务的已完成状态。",
        "bizTag": "task"
    },
    {
        "name": "查询指定任务",
        "detail": "该接口用于获取任务详情，包括任务标题、描述、时间、来源等信息。",
        "bizTag": "task"
    },
    {
        "name": "查询所有任务",
        "detail": "以分页的方式获取任务列表。当使用user_access_token时，获取与该用户身份相关的所有任务。当使用tenant_access_token时，获取以该应用身份通过“创建任务“接口创建的所有任务（并非获取该应用所在租户下所有用户创建的任务）。\n本接口支持通过任务创建时间以及任务的完成状态对任务进行过滤。",
        "bizTag": "task"
    },
    {
        "name": "新增提醒时间",
        "detail": "该接口用于创建任务的提醒时间。提醒时间在截止时间基础上做偏移，但是偏移后的结果不能早于当前时间。",
        "bizTag": "task"
    },
    {
        "name": "删除提醒时间",
        "detail": "删除提醒时间，返回结果状态。",
        "bizTag": "task"
    },
    {
        "name": "查询提醒时间列表",
        "detail": "返回提醒时间列表，支持分页，最大值为50。",
        "bizTag": "task"
    },
    {
        "name": "创建评论",
        "detail": "该接口用于创建和回复任务的评论。当parent_id字段为0时，为创建评论；当parent_id不为0时，为回复某条评论。",
        "bizTag": "task"
    },
    {
        "name": "删除评论",
        "detail": "该接口用于通过评论ID删除评论。",
        "bizTag": "task"
    },
    {
        "name": "更新评论",
        "detail": "该接口用于更新评论内容。",
        "bizTag": "task"
    },
    {
        "name": "获取评论详情",
        "detail": "该接口用于通过评论ID获取评论详情。",
        "bizTag": "task"
    },
    {
        "name": "获取评论列表",
        "detail": "该接口用于查询任务评论列表，支持分页，最大值为100。",
        "bizTag": "task"
    },
    {
        "name": "新增关注人",
        "detail": "该接口用于创建任务关注人。可以一次性添加多位关注人。关注人ID要使用表示用户的ID。",
        "bizTag": "task"
    },
    {
        "name": "删除指定关注人",
        "detail": "该接口用于删除任务关注人。",
        "bizTag": "task"
    },
    {
        "name": "批量删除关注人",
        "detail": "该接口用于批量删除关注人。",
        "bizTag": "task"
    },
    {
        "name": "获取关注人列表",
        "detail": "该接口用于查询任务关注人列表，支持分页，最大值为50。",
        "bizTag": "task"
    },
    {
        "name": "新增执行者",
        "detail": "该接口用于新增任务执行者，一次性可以添加多个执行者。\n只有任务的创建者和执行者才能添加执行者，关注人无权限添加。",
        "bizTag": "task"
    },
    {
        "name": "删除指定执行者",
        "detail": "该接口用于删除任务执行者。",
        "bizTag": "task"
    },
    {
        "name": "批量删除执行者",
        "detail": "该接口用于批量删除执行者。",
        "bizTag": "task"
    },
    {
        "name": "获取执行者列表",
        "detail": "该接口用于查询任务执行者列表，支持分页，最大值为50。",
        "bizTag": "task"
    },
    {
        "name": "获取 user_access_token",
        "detail": "",
        "bizTag": "auth"
    },
    {
        "name": "刷新 user_access_token",
        "detail": "",
        "bizTag": "auth"
    },
    {
        "name": "获取登录预授权码",
        "detail": "应用请求用户身份验证时，需构造登录链接，并引导用户跳转至此链接。用户登录成功后会生成登录预授权码 code，并作为参数追加到重定向URL。",
        "bizTag": "auth"
    },
    {
        "name": "获取 user_access_token（v1 版本）",
        "detail": "根据[登录预授权码](/ssl:ttdoc/ukTMukTMukTM/ukzN4UjL5cDO14SO3gTN) code 获取 `user_access_token`。",
        "bizTag": "auth"
    },
    {
        "name": "刷新 user_access_token（v1 版本）",
        "detail": "`user_access_token` 的最大有效期是 6900 秒。当 `user_access_token` 过期时，可以调用本接口获取新的 `user_access_token`。",
        "bizTag": "auth"
    },
    {
        "name": "创建草稿",
        "detail": "草稿并非词条，而是指通过 API 发起创建新词条或更新现有词条的申请。\n词典管理员审核通过后，草稿将变为新的词条或覆盖已有词条。",
        "bizTag": "baike"
    },
    {
        "name": "更新草稿",
        "detail": "根据 draft_id 更新草稿内容，已审批的草稿无法编辑。",
        "bizTag": "baike"
    },
    {
        "name": "创建免审词条",
        "detail": "通过此接口创建的词条，无需经过词典管理员审核，直接写入词库。因此，调用此接口时，应当慎重操作。",
        "bizTag": "baike"
    },
    {
        "name": "更新免审词条",
        "detail": "通过此接口更新已有的词条，无需经过词典管理员审核，直接写入词库。\n因此，调用该接口时应当慎重操作。",
        "bizTag": "baike"
    },
    {
        "name": "获取词条详情",
        "detail": "通过词条 id 拉取对应的词条详情信息。",
        "bizTag": "baike"
    },
    {
        "name": "获取词条列表",
        "detail": "分页拉取词条列表数据，支持拉取租户内的全部词条。",
        "bizTag": "baike"
    },
    {
        "name": "精准搜索词条",
        "detail": "将关键词与词条名、别名精准匹配，并返回对应的 词条 ID。",
        "bizTag": "baike"
    },
    {
        "name": "模糊搜索词条",
        "detail": "传入关键词，与词条名、别名、释义等信息进行模糊匹配，返回搜到的词条信息。",
        "bizTag": "baike"
    },
    {
        "name": "词条高亮",
        "detail": "传入一句话，智能识别句中对应的词条，并返回词条位置和 entity_id，可在外部系统中快速实现词条智能高亮。",
        "bizTag": "baike"
    },
    {
        "name": "提取潜在的词条",
        "detail": "提取文本中可能成为词条的词语，且不会过滤已经成为词条的词语。同时返回推荐的别名。",
        "bizTag": "baike"
    },
    {
        "name": "获取词典分类",
        "detail": "获取飞书词典当前分类。<br>\n飞书词典目前为二级分类体系，每个词条可添加多个二级分类，但选择的二级分类必须从属于不同的一级分类。",
        "bizTag": "baike"
    },
    {
        "name": "上传图片",
        "detail": "词条图片资源上传。",
        "bizTag": "baike"
    },
    {
        "name": "下载图片",
        "detail": "通过 file_token 下载原图片。",
        "bizTag": "baike"
    },
    {
        "name": "获取企业安装的应用",
        "detail": "查询企业安装的应用列表，只能被企业自建应用调用。",
        "bizTag": "application"
    },
    {
        "name": "更新应用可用范围",
        "detail": "增加或者删除指定应用被哪些人可用，只能被企业自建应用调用。",
        "bizTag": "application"
    },
    {
        "name": "订阅审批事件",
        "detail": "应用订阅 approval_code 后，该应用就可以收到该审批定义对应实例的事件通知。同一应用只需要订阅一次，无需重复订阅。",
        "bizTag": "approval"
    },
    {
        "name": "取消订阅审批事件",
        "detail": "取消订阅 approval_code 后，无法再收到该审批定义对应实例的事件通知。",
        "bizTag": "approval"
    },
    {
        "name": "查看审批定义",
        "detail": "根据 Approval Code 获取某个审批定义的详情，用于构造创建审批实例的请求。",
        "bizTag": "approval"
    },
    {
        "name": "创建审批实例",
        "detail": "创建一个审批实例，调用方需对审批定义的表单有详细了解，将按照定义的表单结构，将表单 Value 通过接口传入。",
        "bizTag": "approval"
    },
    {
        "name": "获取单个审批实例详情",
        "detail": "通过审批实例 Instance Code  获取审批实例详情。Instance Code 由 批量获取审批实例 接口获取。",
        "bizTag": "approval"
    },
    {
        "name": "批量获取审批实例ID",
        "detail": "根据 approval_code 批量获取审批实例的 instance_code，用于拉取租户下某个审批定义的全部审批实例。默认以审批创建时间排序。",
        "bizTag": "approval"
    },
    {
        "name": "审批实例抄送",
        "detail": "通过接口可以将当前审批实例抄送给其他人。",
        "bizTag": "approval"
    },
    {
        "name": "审批实例撤回",
        "detail": "对于状态为“审批中”的单个审批实例进行撤销操作，撤销后审批流程结束。",
        "bizTag": "approval"
    },
    {
        "name": "审批任务同意",
        "detail": "对于单个审批任务进行同意操作。同意后审批流程会流转到下一个审批人。",
        "bizTag": "approval"
    },
    {
        "name": "审批任务拒绝",
        "detail": "对于单个审批任务进行拒绝操作。拒绝后审批流程结束。",
        "bizTag": "approval"
    },
    {
        "name": "审批任务转交",
        "detail": "对于单个审批任务进行转交操作。转交后审批流程流转给被转交人。",
        "bizTag": "approval"
    },
    {
        "name": "三方审批定义创建",
        "detail": "审批定义是审批的描述，包括审批名称、图标、描述等基础信息。创建好审批定义，用户就可以在审批应用的发起页中看到审批，如果用户点击发起，则会跳转到配置的发起三方系统地址去发起审批。另外，审批定义还配置了审批操作时的回调地址：审批人在待审批列表中进行【同意】【拒绝】操作时，审批中心会调用回调地址通知三方系统。",
        "bizTag": "approval"
    },
    {
        "name": "三方审批实例同步",
        "detail": "审批中心不负责审批的流转，审批的流转在三方系统，三方系统在审批流转后生成的审批实例、审批任务、审批抄送数据同步到审批中心。用户可以在审批中心中浏览三方系统同步过来的实例、任务、抄送信息，并且可以跳转回三方系统进行更详细的查看和操作，其中实例信息在【已发起】列表，任务信息在【待审批】和【已审批】列表，抄送信息在【抄送我】列表。",
        "bizTag": "approval"
    },
    {
        "name": "三方审批实例校验",
        "detail": "校验三方审批实例数据，用于判断服务端数据是否为最新的。用户提交实例最新更新时间，如果服务端不存在该实例，或者服务端实例更新时间不是最新的，则返回对应实例 id。",
        "bizTag": "approval"
    },
    {
        "name": "获取三方审批任务状态",
        "detail": "获取三方审批的状态。用户传入查询条件，接口返回满足条件的审批实例的状态。",
        "bizTag": "approval"
    },
    {
        "name": "创建审批定义",
        "detail": "通过接口创建简单的审批定义，可以灵活指定定义的基础信息、表单和流程等。不推荐企业自建应用使用，如有需要尽量联系管理员在审批管理后台创建定义。",
        "bizTag": "approval"
    },
    {
        "name": "实例列表查询",
        "detail": "通过不同条件查询审批系统中符合条件的审批实例列表。",
        "bizTag": "approval"
    },
    {
        "name": "抄送列表查询",
        "detail": "通过不同条件查询审批系统中符合条件的审批抄送列表。",
        "bizTag": "approval"
    },
    {
        "name": "任务列表查询",
        "detail": "通过不同条件查询审批系统中符合条件的审批任务列表。",
        "bizTag": "approval"
    },
    {
        "name": "获取用户列表",
        "detail": "基于部门ID获取部门下直属用户列表。\n[常见问题答疑](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN)。",
        "bizTag": "contact"
    },
    {
        "name": "获取角色列表",
        "detail": "获取企业的用户角色列表。",
        "bizTag": "contact"
    },
    {
        "name": "更新用户所有信息",
        "detail": "该接口用于更新通讯录中用户的字段。",
        "bizTag": "contact"
    },
    {
        "name": "获取部门信息列表",
        "detail": "该接口用于获取当前部门子部门列表。[常见问题答疑](/ssl:ttdoc/ugTN1YjL4UTN24CO1UjN/uQzN1YjL0cTN24CN3UjN)。",
        "bizTag": "contact"
    },
    {
        "name": "批量新增部门",
        "detail": "向通讯录中批量新增多个部门。",
        "bizTag": "contact"
    },
    {
        "name": "批量新增用户",
        "detail": "向通讯录中批量新增多个用户。",
        "bizTag": "contact"
    },
    {
        "name": "查询批量任务执行状态",
        "detail": "查询通讯录异步任务当前的执行状态以及执行结果。",
        "bizTag": "contact"
    },
    {
        "name": "检索记录",
        "detail": "该接口用于根据 record_id 的值检索现有记录",
        "bizTag": "base"
    },
    {
        "name": "列出记录",
        "detail": "该接口用于列出数据表中的现有记录，单次最多列出 500 行记录，支持分页获取。",
        "bizTag": "base"
    },
    {
        "name": "创建旧版文档",
        "detail": "创建并初始化文档。",
        "bizTag": "ccm"
    },
    {
        "name": "获取旧版文档元信息",
        "detail": "根据 docToken 获取元数据。",
        "bizTag": "ccm"
    },
    {
        "name": "获取旧版文档中的电子表格元数据",
        "detail": "根据 docToken 获取文档中的电子表格的元数据。",
        "bizTag": "ccm"
    },
    {
        "name": "获取旧版文档纯文本内容",
        "detail": "获取文档的纯文本内容，不包含富文本格式信息。",
        "bizTag": "ccm"
    },
    {
        "name": "获取旧版文档富文本内容",
        "detail": "获取结构化的文档内容。",
        "bizTag": "ccm"
    },
    {
        "name": "编辑旧版文档内容",
        "detail": "批量编辑更新文档内容，包括更新标题、范围删除、插入内容。",
        "bizTag": "ccm"
    },
    {
        "name": "获取表格元数据",
        "detail": "根据 spreadsheetToken 获取表格元数据。",
        "bizTag": "ccm"
    },
    {
        "name": "更新表格属性",
        "detail": "根据 spreadsheetToken 更新表格属性，如更新表格标题。",
        "bizTag": "ccm"
    },
    {
        "name": "导入表格",
        "detail": "将本地表格导入到云空间上。",
        "bizTag": "ccm"
    },
    {
        "name": "查询导入结果",
        "detail": "查询文件导入结果。查询30分钟无结果为导入失败。",
        "bizTag": "ccm"
    },
    {
        "name": "新建文件",
        "detail": "根据 folderToken 创建 Doc、 Sheet 或 Bitable 。",
        "bizTag": "ccm"
    },
    {
        "name": "获取元数据",
        "detail": "根据 token 获取各类文件的元数据。",
        "bizTag": "ccm"
    },
    {
        "name": "删除Sheet",
        "detail": "根据 spreadsheetToken 删除对应的 sheet 文档。",
        "bizTag": "ccm"
    },
    {
        "name": "复制文档",
        "detail": "根据文件 token 复制 Doc 或 Sheet  到目标文件夹中。若没有特定的文件夹用于承载创建的文档，可以先调用「获取文件夹元信息」文档中的「获取 root folder (我的空间) meta」接口，获得我的空间的 token，然后再使用此接口。复制的文档将会在「我的空间」的「归我所有」列表里。",
        "bizTag": "ccm"
    },
    {
        "name": "删除Doc",
        "detail": "根据 docToken 删除对应的 Docs 文档。",
        "bizTag": "ccm"
    },
    {
        "name": "获取文件夹下的文档清单",
        "detail": "根据 folderToken 获取该文件夹的文档清单，如 doc、sheet、file、bitable、folder。",
        "bizTag": "ccm"
    },
    {
        "name": "新建文件夹",
        "detail": "根据 folderToken 在该 folder 下创建文件夹。",
        "bizTag": "ccm"
    },
    {
        "name": "判断协作者是否有某权限",
        "detail": "根据 filetoken 判断当前登录用户是否具有某权限。",
        "bizTag": "ccm"
    },
    {
        "name": "转移拥有者",
        "detail": "根据文档信息和用户信息转移文档的所有者。",
        "bizTag": "ccm"
    },
    {
        "name": "获取云文档权限设置V2",
        "detail": "根据 filetoken 获取文档的公共设置。",
        "bizTag": "ccm"
    },
    {
        "name": "获取面试记录列表",
        "detail": "根据投递 ID 获取面试记录列表",
        "bizTag": "hire"
    },
    {
        "name": "查询人才操作记录",
        "detail": "查询操作人对人才的操作记录。",
        "bizTag": "hire"
    },
    {
        "name": "获取职位上的招聘人员信息",
        "detail": "根据职位 ID 获取职位上的招聘人员信息，如招聘负责人、用人经理。",
        "bizTag": "hire"
    },
    {
        "name": "获取 Offer 申请表详细信息",
        "detail": "根据 Offer 申请表 ID，获取 Offer 申请表的详细信息",
        "bizTag": "hire"
    },
    {
        "name": "获取流程表单数据",
        "detail": "获取流程表单数据。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询城市/区域信息",
        "detail": "批量查询城市/区域信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单条城市/区域信息",
        "detail": "查询单条城市/区域信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询省份/行政区信息",
        "detail": "批量查询省份/行政区信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单条省份/行政区信息",
        "detail": "查询单条省份/行政区信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询国家/地区信息",
        "detail": "批量查询国家/地区信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单条国家/地区信息",
        "detail": "查询单条国家/地区信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询货币信息",
        "detail": "批量查询货币信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个货币信息",
        "detail": "查询单个货币信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个职务",
        "detail": "根据 ID 查询单个职务。",
        "bizTag": "feishu_people"
    },
    {
        "name": "删除部门",
        "detail": "删除部门",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新部门",
        "detail": "更新部门。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个部门",
        "detail": "根据 ID 查询单个部门。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询职务",
        "detail": "批量查询职务。",
        "bizTag": "feishu_people"
    },
    {
        "name": "批量查询部门",
        "detail": "批量查询部门。",
        "bizTag": "feishu_people"
    },
    {
        "name": "更新个人信息",
        "detail": "更新个人信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "创建个人信息",
        "detail": "创建人员的个人信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "查询单个个人信息",
        "detail": "根据 ID 查询单个人员的个人信息。",
        "bizTag": "feishu_people"
    },
    {
        "name": "操作员工离职",
        "detail": "操作员工直接离职。",
        "bizTag": "feishu_people"
    },
    {
        "name": "获取建筑物列表",
        "detail": "获取本企业下的建筑物（办公大楼）。",
        "bizTag": "meeting_room"
    },
    {
        "name": "查询建筑物详情",
        "detail": "获取指定建筑物的详细信息。",
        "bizTag": "meeting_room"
    },
    {
        "name": "获取会议室列表",
        "detail": "获取指定建筑下的会议室。",
        "bizTag": "meeting_room"
    },
    {
        "name": "查询会议室详情",
        "detail": "获取指定会议室的详细信息。",
        "bizTag": "meeting_room"
    },
    {
        "name": "创建建筑物",
        "detail": "对应管理后台的添加建筑，添加楼层的功能，可用于创建建筑物和建筑物的楼层信息。",
        "bizTag": "meeting_room"
    },
    {
        "name": "更新建筑物",
        "detail": "编辑建筑信息，添加楼层，删除楼层，编辑楼层信息。",
        "bizTag": "meeting_room"
    },
    {
        "name": "删除建筑物",
        "detail": "删除建筑物（办公大楼）。",
        "bizTag": "meeting_room"
    },
    {
        "name": "查询建筑物ID",
        "detail": "根据租户自定义建筑 ID 查询建筑 ID。",
        "bizTag": "meeting_room"
    },
    {
        "name": "创建会议室",
        "detail": "创建会议室。",
        "bizTag": "meeting_room"
    },
    {
        "name": "更新会议室",
        "detail": "更新会议室。",
        "bizTag": "meeting_room"
    },
    {
        "name": "删除会议室",
        "detail": "删除会议室。",
        "bizTag": "meeting_room"
    },
    {
        "name": "查询会议室ID",
        "detail": "根据租户自定义会议室ID查询会议室ID。",
        "bizTag": "meeting_room"
    },
    {
        "name": "获取国家地区列表",
        "detail": "新建建筑时需要标明所处国家/地区，该接口用于获得系统预先提供的可供选择的国家 /地区列表。",
        "bizTag": "meeting_room"
    },
    {
        "name": "获取城市列表",
        "detail": "新建建筑时需要选择所处国家/地区，该接口用于获得系统预先提供的可供选择的城市列表。",
        "bizTag": "meeting_room"
    },
    {
        "name": "创建签到板部署码",
        "detail": "创建一个范围内的签到板部署码",
        "bizTag": "vc"
    },
    {
        "name": "创建会议室部署码",
        "detail": "创建一个范围内的会议室部署码",
        "bizTag": "vc"
    },
    {
        "name": "查询会议室配置",
        "detail": "查询一个范围内的会议室配置。",
        "bizTag": "vc"
    },
    {
        "name": "设置会议室配置",
        "detail": "设置一个范围内的会议室配置。",
        "bizTag": "vc"
    }
]