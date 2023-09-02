from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, INTEGER
from flask_login import UserMixin

class Player(db.Model, UserMixin):
    __tablename__ = 'players'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    group_id = db.Column(db.Integer, default=0)
    account_id = db.Column(db.Integer, nullable=False) # Change to forignkey
    level = db.Column(db.Integer, nullable=False, default=1)
    vocation = db.Column(db.Integer, nullable=False, default=0)
    health = db.Column(db.Integer, nullable=False, default=150)
    healthmax = db.Column(db.Integer, nullable=False, default=150)
    experience = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    lookbody = db.Column(db.Integer, nullable=False)
    lookfeet = db.Column(db.Integer, nullable=False)
    lookhead = db.Column(db.Integer, nullable=False)
    looklegs = db.Column(db.Integer, nullable=False)
    looktype = db.Column(db.Integer, nullable=False, default=136)
    lookaddons = db.Column(db.Integer, nullable=False)
    direction = db.Column(SMALLINT(unsigned=True), nullable=False, default=2)
    maglevel = db.Column(db.Integer, nullable=False)
    mana = db.Column(db.Integer, nullable=False, default=0)
    manamax = db.Column(db.Integer, nullable=False, default=0)
    manaspent = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    soul = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    town_id = db.Column(db.Integer, nullable=False, default=1)
    posx = db.Column(db.Integer, nullable=False, default=0)
    posy = db.Column(db.Integer, nullable=False, default=0)
    posz = db.Column(db.Integer, nullable=False, default=0)
    conditions = db.Column(db.LargeBinary)
    cap = db.Column(db.Integer, nullable=False, default=400)
    sex = db.Column(db.Integer, nullable=False, default=0)
    lastlogin = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    lastip = db.Column(INTEGER(unsigned=True), nullable=False, default=0)
    save = db.Column(db.SmallInteger, nullable=False, default=1)
    skull = db.Column(db.SmallInteger, nullable=False, default=0)
    skulltime = db.Column(db.BigInteger, nullable=False, default=0)
    lastlogout = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    blessings = db.Column(db.SmallInteger, nullable=False, default=0)
    onlinetime = db.Column(db.BigInteger, nullable=False, default=0)
    deletion = db.Column(db.BigInteger, nullable=False, default=0)
    balance = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    offlinetraining_time = db.Column(SMALLINT(unsigned=True), nullable=False, default=43200)
    offlinetraining_skill = db.Column(db.Integer, nullable=False, default=-1)
    stamina = db.Column(SMALLINT(unsigned=True), nullable=False, default=2520)
    
    skill_fist = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_fist_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_club = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_club_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_sword = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_sword_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_axe = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_axe_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_dist = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_dist_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_shielding = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_shielding_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)
    skill_fishing = db.Column(INTEGER(unsigned=True), nullable=False, default=10)
    skill_fishing_tries = db.Column(BIGINT(unsigned=True), nullable=False, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'group_id': self.group_id,
            'account_id': self.account_id,
            'level': self.level,
            'vocation': self.vocation,
            'health': self.health,
            'healthmax': self.healthmax,
            'experience': self.experience,
            'lookbody': self.lookbody,
            'lookfeet': self.lookfeet,
            'lookhead': self.lookhead,
            'looklegs': self.looklegs,
            'looktype': self.looktype,
            'lookaddons': self.lookaddons,
            'direction': self.direction,
            'maglevel': self.maglevel,
            'mana': self.mana,
            'manamax': self.manamax,
            'manaspent': self.manaspent,
            'soul': self.soul,
            'town_id': self.town_id,
            'posx': self.posx,
            'posy': self.posy,
            'posz': self.posz,
            'conditions': self.conditions,
            'cap': self.cap,
            'sex': self.sex,
            'lastlogin': self.lastlogin,
            'lastip': self.lastip,
            'save': self.save,
            'skull': self.skull,
            'skulltime': self.skulltime,
            'lastlogout': self.lastlogout,
            'blessings': self.blessings,
            'onlinetime': self.onlinetime,
            'deletion': self.deletion,
            'balance': self.balance,
            'offlinetraining_time': self.offlinetraining_time,
            'offlinetraining_skill': self.offlinetraining_skill,
            'stamina': self.stamina,
            'skill_fist': self.skill_fist,
            'skill_fist_tries': self.skill_fist_tries,
            'skill_club': self.skill_club,
            'skill_club_tries': self.skill_club_tries,
            'skill_sword': self.skill_sword,
            'skill_sword_tries': self.skill_sword_tries,
            'skill_axe': self.skill_axe,
            'skill_axe_tries': self.skill_axe_tries,
            'skill_dist': self.skill_dist,
            'skill_dist_tries': self.skill_dist_tries,
            'skill_shielding': self.skill_shielding,
            'skill_shielding_tries': self.skill_shielding_tries,
            'skill_fishing': self.skill_fishing,
            'skill_fishing_tries': self.skill_fishing_tries
        }
