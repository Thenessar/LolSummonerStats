-- Table: public.summoners

-- DROP TABLE IF EXISTS public.summoners;

CREATE TABLE IF NOT EXISTS public.summoners
(
    accountid character varying(56) COLLATE pg_catalog."default",
    profileiconid integer,
    revisiondate bigint,
    name character varying(60) COLLATE pg_catalog."default",
    puuid character varying(78) COLLATE pg_catalog."default",
    summonerlevel bigint,
    id uuid NOT NULL,
    CONSTRAINT pk_summoners_id PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.summoners
    OWNER to postgres;
-- Index: hash_summoners_name

-- DROP INDEX IF EXISTS public.hash_summoners_name;

CREATE INDEX IF NOT EXISTS hash_summoners_name
    ON public.summoners USING hash
    (name COLLATE pg_catalog."default")
    TABLESPACE pg_default;
-- Index: hash_summoners_puuid

-- DROP INDEX IF EXISTS public.hash_summoners_puuid;

CREATE INDEX IF NOT EXISTS hash_summoners_puuid
    ON public.summoners USING hash
    (puuid COLLATE pg_catalog."default")
    TABLESPACE pg_default;


-- Table: public.games

-- DROP TABLE IF EXISTS public.games;

CREATE TABLE IF NOT EXISTS public.games
(
    participants character varying(78)[] COLLATE pg_catalog."default",
    gamecreation bigint,
    gameduration bigint,
    gameendtimestamp bigint,
    gamemode character varying(80) COLLATE pg_catalog."default",
    gamename character varying(80) COLLATE pg_catalog."default",
    gamestarttimestamp bigint,
    gametype character varying(80) COLLATE pg_catalog."default",
    gameversion character varying(80) COLLATE pg_catalog."default",
    mapid integer,
    queueid integer,
    teams integer[],
    id uuid NOT NULL,
    CONSTRAINT pk_games_id PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.games
    OWNER to postgres;	
	

-- Table: public.game_teams

-- DROP TABLE IF EXISTS public.game_teams;

CREATE TABLE IF NOT EXISTS public.game_teams
(
    firstbaron boolean,
    firstchampion boolean,
    firstdragon boolean,
    firstinhibitor boolean,
    firstriftherald boolean,
    firsttower boolean,
    baronkills integer,
    championkills integer,
    dragonkills integer,
    inhibitorkills integer,
    riftheraldkills integer,
    towerkills integer,
    win boolean,
    id uuid NOT NULL,
    gameid uuid NOT NULL,
    side character varying(10) COLLATE pg_catalog."default",
    CONSTRAINT pk_game_teams_id PRIMARY KEY (id),
    CONSTRAINT fk_game_teams_gameid FOREIGN KEY (gameid)
        REFERENCES public.games (id) MATCH FULL
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_teams
    OWNER to postgres;	


-- Table: public.game_participants

-- DROP TABLE IF EXISTS public.game_participants;

CREATE TABLE IF NOT EXISTS public.game_participants
(
    puuid character varying(78) COLLATE pg_catalog."default" NOT NULL,
    assists integer,
    baronkills integer,
    bountylevel integer,
    champexperience integer,
    champlevel integer,
    championid integer,
    championname character varying(80) COLLATE pg_catalog."default",
    championtransform integer,
    consumablespurchased integer,
    damagedealttobuildings integer,
    damagedealttoobjectives integer,
    damagedealttoturrets integer,
    damageselfmitigated integer,
    deaths integer,
    detectorwardsplaced integer,
    doublekills integer,
    dragonkills integer,
    firstbloodassist boolean,
    firstbloodkill boolean,
    firsttowerassist boolean,
    firsttowerkill boolean,
    gameendedinearlysurrender boolean,
    gameendedinsurrender boolean,
    goldearned integer,
    goldspent integer,
    individualposition character varying(40) COLLATE pg_catalog."default",
    inhibitorkills integer,
    inhibitortakedowns integer,
    inhibitorslost integer,
    item0 integer,
    item1 integer,
    item2 integer,
    item3 integer,
    item4 integer,
    item5 integer,
    item6 integer,
    itemspurchased integer,
    killingsprees integer,
    kills integer,
    lane character varying(40) COLLATE pg_catalog."default",
    largestcriticalstrike integer,
    largestkillingspree integer,
    largestmultikill integer,
    longesttimespentliving integer,
    magicdamagedealt integer,
    magicdamagedealttochampions integer,
    magicdamagetaken integer,
    neutralminionskilled integer,
    nexuskills integer,
    nexustakedowns integer,
    nexuslost integer,
    objectivesstolen integer,
    objectivesstolenassists integer,
    participantid integer,
    pentakills integer,
    physicaldamagedealt integer,
    physicaldamagedealttochampions integer,
    physicaldamagetaken integer,
    profileicon integer,
    quadrakills integer,
    riotidname character varying(80) COLLATE pg_catalog."default",
    riotidtagline character varying(80) COLLATE pg_catalog."default",
    role character varying(40) COLLATE pg_catalog."default",
    sightwardsboughtingame integer,
    spell1casts integer,
    spell2casts integer,
    spell3casts integer,
    spell4casts integer,
    summoner1casts integer,
    summoner1id integer,
    summoner2casts integer,
    summoner2id integer,
    summonerlevel integer,
    summonername character varying(80) COLLATE pg_catalog."default",
    teamearlysurrendered boolean,
    teamid integer,
    teamposition character varying(40) COLLATE pg_catalog."default",
    timeccingothers integer,
    timeplayed integer,
    totaldamagedealt integer,
    totaldamagedealttochampions integer,
    totaldamageshieldedonteammates integer,
    totaldamagetaken integer,
    totalheal integer,
    totalhealsonteammates integer,
    totalminionskilled integer,
    totaltimeccdealt integer,
    totaltimespentdead integer,
    totalunitshealed integer,
    triplekills integer,
    truedamagedealt integer,
    truedamagedealttochampions integer,
    truedamagetaken integer,
    turretkills integer,
    turrettakedowns integer,
    turretslost integer,
    unrealkills integer,
    visionscore integer,
    visionwardsboughtingame integer,
    wardskilled integer,
    wardsplaced integer,
    win boolean,
    id uuid NOT NULL,
    gameteamid uuid NOT NULL,
    summonerid uuid NOT NULL,
    CONSTRAINT pk_game_participants_id PRIMARY KEY (id),
    CONSTRAINT fk_game_participants_gameteamid FOREIGN KEY (gameteamid)
        REFERENCES public.game_teams (id) MATCH FULL
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_game_participants_summonerid FOREIGN KEY (summonerid)
        REFERENCES public.summoners (id) MATCH FULL
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.game_participants
    OWNER to postgres;
-- Index: hash_game_participants_teamid

-- DROP INDEX IF EXISTS public.hash_game_participants_teamid;

CREATE INDEX IF NOT EXISTS hash_game_participants_teamid
    ON public.game_participants USING hash
    (teamid)
    TABLESPACE pg_default;	
	

-- Table: public.challenges

-- DROP TABLE IF EXISTS public.challenges;

CREATE TABLE IF NOT EXISTS public.challenges
(
    abilityuses integer,
    barontakedowns integer,
    buffsstolen integer,
    controlwardtimecoverageinriverorenemyhalf numeric(40,20),
    controlwardsplaced integer,
    damageperminute numeric(40,20),
    damagetakenonteampercentage numeric(40,20),
    dragontakedowns integer,
    enemyjunglemonsterkills integer,
    firstturretkilledtime numeric(40,20),
    gamelength numeric(40,20),
    gettakedownsinalllanesearlyjungleaslaner integer,
    goldperminute numeric(40,20),
    initialbuffcount integer,
    initialcrabcount integer,
    junglecsbefore10minutes integer,
    kda numeric(40,20),
    killafterhiddenwithally integer,
    killparticipation numeric(40,20),
    killsnearenemyturret integer,
    killsonotherlanesearlyjungleaslaner integer,
    laneminionsfirst10minutes integer,
    legendarycount integer,
    lostaninhibitor integer,
    maxkilldeficit integer,
    moreenemyjunglethanopponent numeric(40,20),
    perfectdragonsoulstaken integer,
    pickkillwithally integer,
    quickfirstturret integer,
    quicksolokills integer,
    riftheraldtakedowns integer,
    saveallyfromdeath integer,
    scuttlecrabkills integer,
    solokill integer,
    stealthwardsplaced integer,
    takedowns integer,
    takedownsaftergainingleveladvantage integer,
    teambaronkills integer,
    teamdamagepercentage numeric(40,20),
    teamelderdragonkills integer,
    teamriftheraldkills integer,
    tooklargedamagesurvived integer,
    turretplatestaken integer,
    turrettakedowns integer,
    turretstakenwithriftherald integer,
    visionscoreperminute numeric(40,20),
    wardtakedowns integer,
    wardtakedownsbefore20m integer,
    earliestdragontakedown integer,
    killsonlanersearlyjungleasjungler integer,
    junglerkillsearlyjungle integer,
    takedownonfirstturret integer,
    id uuid NOT NULL,
    gameparticipantid uuid NOT NULL,
    CONSTRAINT pk_challenges_id PRIMARY KEY (id),
    CONSTRAINT fk_challenges_gameparticipantid FOREIGN KEY (gameparticipantid)
        REFERENCES public.game_participants (id) MATCH FULL
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.challenges
    OWNER to postgres;

	
-- View: public.details

-- DROP VIEW public.details;

CREATE OR REPLACE VIEW public.details
 AS
 SELECT s.name,
    s.puuid,
    s.id,
    gp.assists,
    gp.baronkills,
    gp.championname,
    gp.damagedealttoobjectives,
    gp.deaths,
    gp.firstbloodassist::integer AS firstbloodassist,
    gp.firstbloodkill::integer AS firstbloodkill,
    gp.firsttowerassist::integer AS firsttowerassist,
    gp.firsttowerkill::integer AS firsttowerkill,
    gp.neutralminionskilled,
    gp.participantid,
    gp.teamid,
    gp.teamposition,
    gp.totaldamagedealttochampions,
    gp.totalminionskilled,
    gp.visionscore,
    gp.visionwardsboughtingame,
    gp.wardskilled,
    gp.wardsplaced,
    gp.win::integer AS win,
    gt.firstbaron::integer AS firstbaronteam,
    gt.firstchampion::integer AS firstchampionteam,
    gt.firstdragon::integer AS firstdragonteam,
    gt.firstinhibitor::integer AS firstinhibitorteam,
    gt.firstriftherald::integer AS firstriftheraldteam,
    gt.firsttower::integer AS firsttowerteam,
    gt.baronkills AS baronkillsteam,
    gt.dragonkills AS dragonkillsteam,
    gt.inhibitorkills AS inhibitorkillsteam,
    gt.riftheraldkills AS riftheraldkillsteam,
    gt.towerkills AS towerkillsteam,
    gt.side,
    g.gameduration AS gamedurationint,
    concat('00:', floor((g.gameduration / 60)::double precision)::character varying(2), ':',
        CASE
            WHEN (g.gameduration % 60::bigint) < 10 THEN concat('0', ((g.gameduration % 60::bigint))::character varying(2))::character varying
            ELSE ((g.gameduration % 60::bigint))::character varying(2)
        END)::time without time zone AS gameduration,
    to_timestamp((g.gamestarttimestamp / 1000)::double precision)::date AS gamedate,
    g.gameversion,
    ch.abilityuses,
    ch.controlwardtimecoverageinriverorenemyhalf,
    ch.damageperminute,
    ch.damagetakenonteampercentage,
    ch.enemyjunglemonsterkills,
    ch.gettakedownsinalllanesearlyjungleaslaner,
    ch.goldperminute,
    ch.initialcrabcount,
    ch.junglecsbefore10minutes,
    ch.kda,
    ch.killafterhiddenwithally,
    (gp.kills::numeric + gp.assists::numeric) / gt.championkills::numeric AS killparticipation,
    ch.killsonotherlanesearlyjungleaslaner,
    ch.laneminionsfirst10minutes,
    ch.perfectdragonsoulstaken,
    ch.pickkillwithally,
    ch.riftheraldtakedowns,
    ch.scuttlecrabkills,
    ch.solokill,
    ch.takedowns,
    ch.teamdamagepercentage,
    ch.teamelderdragonkills,
    ch.teamriftheraldkills,
    ch.turretplatestaken,
    ch.turrettakedowns,
    ch.visionscoreperminute,
    ch.earliestdragontakedown,
    ch.killsonlanersearlyjungleasjungler,
    ch.takedownonfirstturret,
	CASE
		WHEN (( SELECT 1
		   FROM game_participants gp2
		  WHERE gp2.gameteamid = gp.gameteamid AND gp2.summonername::text = 'Adben'::text
		 LIMIT 1)) = 1 THEN 'Team with Adben'::text
		ELSE 'Team without Adben'::text
	END AS teamname,
	CASE
		WHEN (( SELECT 1
		   FROM game_participants gp2
		  WHERE gp2.gameteamid = gp.gameteamid AND gp.teamposition = 'JUNGLE' AND gp2.summonername::text = 'Adben'::text
		 LIMIT 1)) = 1 THEN 'Adben'::text
		ELSE 'Other junglers'::text
	END AS playertype,
	CASE
		WHEN (( SELECT 1
		   FROM game_participants gp2
		  WHERE gp2.gameteamid = gp.gameteamid AND gp2.summonername::text = 'Adben'::text AND (EXISTS ( SELECT
				   FROM game_participants gp3
				  WHERE gp3.gameteamid = gp2.gameteamid AND (gp3.summonername::text = ANY (ARRAY['Enthelin'::character varying::text, 'Golonka'::character varying::text, 'Archen'::character varying::text, 'Bastrard'::character varying::text, 'Bulwers'::character varying::text, 'ButcherOfVatiken'::character varying::text, 'Nedoraenota'::character varying::text, 'TopOfDaFoodChain'::character varying::text]))))
		 LIMIT 1)) = 1 THEN 'Duo'::text
		ELSE 'Solo'::text
	END AS queuetype
   FROM summoners s
     JOIN game_participants gp ON gp.summonerid = s.id
     JOIN game_teams gt ON gt.id = gp.gameteamid
     JOIN games g ON g.id = gt.gameid
     JOIN challenges ch ON ch.gameparticipantid = gp.id;

ALTER TABLE public.details
    OWNER TO postgres;
	
	

