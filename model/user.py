from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    VARCHAR,
    ForeignKey, Date, Index, Float, event, func,
)

from model.db import Base


class User(Base):  # 用户表
    __tablename__ = 'user'
    __table_args__ = (
        Index('ix_user_has_delete_username', "has_delete", "username"),  # 非唯一的联合索引
        Index('ix_user_has_delete_email', "has_delete", "email")
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    username = Column(VARCHAR(32), nullable=False, unique=True, comment='用户名')  # 用户名，非空，唯一
    password = Column(VARCHAR(128), nullable=False, comment='密码')  # 密码，非空
    email = Column(VARCHAR(64), nullable=False, unique=True, comment='邮箱地址')  # 邮箱，非空，唯一
    card_id = Column(VARCHAR(32), nullable=True, unique=True, comment='学号或工号，SDU+学号')  # 学号，可空，唯一
    registration_dt = Column(DateTime, nullable=False, comment='注册时间，新建时自动填写', default=func.now())  # 注册时间，非空
    storage_quota = Column(Integer, nullable=False, comment='存储空间限制（MB）', default=32)  # 存储空间限制（MB），非空
    status = Column(Integer, nullable=False, index=True,
                    comment='是否已经禁用:0 正常使用,1 账号未激活,2 账号已注销,3 账号被封禁,', default=1)  # 账号状态，非空
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空



class User_info(Base):  # 用户信息表
    __tablename__ = 'user_info'
    __table_args__ = (
        Index('ix_user_info_has_delete_major_id_class_id', "has_delete", "major_id", "class_id"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True, comment='外键，用户id')  # 用户id,外键，非空
    realname = Column(VARCHAR(32), nullable=False, comment='真实姓名')  # 真实姓名，非空
    gender = Column(Integer, nullable=False, comment='性别:0 男性 (Male),1 女性 (Female),2 其他 (Other)')  # 性别，非空
    major_id = Column(Integer, ForeignKey('major.id'), nullable=True, comment='专业id，外键')  # 专业id，外键，可空
    class_id = Column(Integer, ForeignKey('class.id'), nullable=True, comment='班级id，外键')  # 班级id，外键，可空
    enrollment_dt = Column(Date, nullable=False, comment='入学时间')  # 入学时间，非空
    graduation_dt = Column(Date, nullable=False, comment='毕业时间')  # 毕业时间，非空
    oj_username = Column(VARCHAR(32), nullable=True, unique=True, comment='oj用户名')  # 用户名，可空，唯一
    oj_password = Column(VARCHAR(1024), nullable=True, comment='oj密码')  # 密码，可空
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空


class School(Base):  # 学校表
    __tablename__ = 'school'
    __table_args__ = (
        Index('ix_school_has_delete_name', "has_delete", "name"),  # 非唯一的联合索引
        Index('ix_school_has_delete_abbreviation', "has_delete", "school_abbreviation"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    name = Column(VARCHAR(64), nullable=False, unique=True, comment='学校名称')  # 学校名称，非空，唯一
    school_abbreviation = Column(VARCHAR(10), nullable=False, comment='学校简称，如SDU')  # 学校简称，非空
    school_logo_id = Column(Integer, ForeignKey('user_file.id'), nullable=False,
                            comment='学校logo')  # 学校logo，非空唯一
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空


class College(Base):  # 学院表
    __tablename__ = 'college'
    __table_args__ = (
        Index('ix_college_has_delete_school_id_name', "has_delete", "school_id", "name"),  # 非唯一的联合索引
        Index('ix_college_school_id_name', "school_id", "name"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False, index=True,
                       comment='外键，学校 ID')  # 外键，学校id，非空，索引
    name = Column(VARCHAR(64), nullable=False, comment='学院名称')  # 学院名称，非空
    college_logo_id = Column(Integer, ForeignKey('user_file.id'), nullable=False,
                             comment='学院logo')  # 学院logo，非空唯一
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空


class Major(Base):  # 专业表
    __tablename__ = 'major'
    __table_args__ = (
        Index('ix_major_has_delete_college_id_name', "has_delete", "college_id", "name"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False, index=True,
                        comment='外键，学院ID')  # 外键，学院id，非空，索引
    name = Column(VARCHAR(64), nullable=False, comment='专业名称')  # 专业名称，非空
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空


class Class(Base):  # 班级表
    __tablename__ = 'class'
    __table_args__ = (
        Index('ix_class_has_delete_college_id_name', "has_delete", "college_id", "name"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    college_id = Column(Integer, ForeignKey('college.id'), nullable=False, index=True,
                        comment='外键，学院ID')  # 外键，学院id，非空，索引
    name = Column(VARCHAR(64), nullable=False, comment='班级名称')  # 班级名称，非空
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否被删除，非空


class Operation(Base):  # 操作表
    __tablename__ = 'operation'
    __table_args__ = (
        Index('ix_user_service_id_type', "oper_user_id", "service_type", "service_id"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    service_type = Column(Integer, nullable=False, index=True, comment='业务类型')  # 业务类型，非空，索引
    service_id = Column(Integer, nullable=True, comment='业务id')  # 业务id，可空
    operation_type = Column(VARCHAR(64), comment='操作类型', nullable=False)  # 操作类型
    func = Column(VARCHAR(512), comment='操作', nullable=False)  # 操作
    parameters = Column(VARCHAR(4 * 1024), comment='操作参数', nullable=False)  # 操作参数
    oper_user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True,
                          comment='操作人 id，外键')  # 操作人 id，外键，非空，索引
    oper_dt = Column(DateTime, nullable=False, comment='操作时间')
    oper_hash = Column(VARCHAR(128), index=True, comment='操作哈希值' ,nullable=False)  # 操作哈希值，索引


class Session(Base):  # session表
    __tablename__ = 'session'
    __table_args__ = (
        Index('ix_session_has_delete_token_s6', "has_delete", "token_s6"),  # 非唯一的联合索引
        Index('ix_session_has_delete_token', "has_delete", "token"),  # 非唯一的联合索引
        Index('ix_session_func_type_has_delete', "func_type", "has_delete"),  # 非唯一的联合索引
    )
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True, comment='外键，用户id')  # 外键，用户id，非空，索引
    file_id = Column(Integer,  nullable=True, index=True,
                     comment='文件id')  # 外键，文件id，可空，索引
    token = Column(VARCHAR(32), unique=True, nullable=False, comment='session唯一识别串')  # token，非空，唯一
    token_s6 = Column(VARCHAR(16), nullable=True, comment='8位短token')  # 邮箱验证码，非空
    use = Column(Integer, nullable=False, comment='使用次数')  # 使用次数，非空
    use_limit = Column(Integer, nullable=True, comment='限制次数，没有限制即为NULL')  # 限制次数，可空
    exp_dt = Column(DateTime, comment='过期时间', nullable=False)  # 过期时间，非空
    ip = Column(VARCHAR(32), comment='客户端ip')  # ip
    user_agent = Column(VARCHAR(256), comment='客户端信息')  # 客户端信息
    create_dt = Column(DateTime, comment='创建时间', default=func.now())  # 创建时间
    func_type = Column(Integer,
                       comment='0 用户登录 session:1 用户邮箱验证 session,2 文件下载 session,3 文件上传 session')  # 操作类型
    has_delete = Column(Integer, nullable=False, comment='是否已经删除', default=0)  # 是否已经删除


class Captcha(Base):  # 验证码表
    __tablename__ = 'captcha'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='主键')  # 主键
    value = Column(VARCHAR(8), nullable=False, comment='验证码值')  # 验证码值，非空
    has_delete = Column(Integer, nullable=False, index=True, comment='是否已经删除', default=0)  # 是否已经删除


class Education_Program(Base):  # 培养方案表
    __tablename__ = 'education_program'
    id = Column(Integer, primary_key=True, comment='培养方案ID')
    major_id = Column(Integer, ForeignKey('major.id'), nullable=False, index=True, unique=True,
                      comment='外键，专业ID')  # 外键，专业id，非空，索引
    thought_political_theory = Column(Float, nullable=True, comment='思想政治理论课')
    college_sports = Column(Float, nullable=True, comment='大学体育')
    college_english = Column(Float, nullable=True, comment='大学英语')
    chinese_culture = Column(Float, nullable=True, comment='国学修养')
    art_aesthetics = Column(Float, nullable=True, comment='艺术审美')
    innovation_entrepreneurship = Column(Float, nullable=True, comment='创新创业')
    humanities = Column(Float, nullable=True, comment='人文学科')
    social_sciences = Column(Float, nullable=True, comment='社会科学')
    scientific_literacy = Column(Float, nullable=True, comment='科学素养')
    information_technology = Column(Float, nullable=True, comment='信息技术')
    general_education_elective = Column(Float, nullable=True, comment='通识教育选修课程')
    major_compulsory_courses = Column(Float, nullable=True, comment='专业必修课程')
    major_elective_courses = Column(Float, nullable=True, comment='专业选修课程')
    key_improvement_courses = Column(Float, nullable=True, comment='重点提升必修课程')
    qilu_entrepreneurship = Column(Float, nullable=True, comment='齐鲁创业')
    jixia_innovation = Column(Float, nullable=True, comment='稷下创新')
    has_delete = Column(Integer, nullable=False, index=True, comment='是否已经删除', default=0)  # 是否被删除，非空
