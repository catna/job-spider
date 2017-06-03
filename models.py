#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String)           # 公司名字
    type = Column(String)           # 公司性质
    size = Column(String)           # 公司规模
    vocation = Column(String)       # 公司行业
    location = Column(String)       # 公司位置
    description = Column(String)    # 公司描述
    source = Column(String)         # 来源
    coid = Column(Integer)          # 来源id
    cohash = Column(Integer)        # hash公司名字

DBSession = sessionmaker(bind=engine)
