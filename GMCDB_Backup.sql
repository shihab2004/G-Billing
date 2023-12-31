PGDMP     /                    z            GMCDB    14.4    14.4 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    32851    GMCDB    DATABASE     k   CREATE DATABASE "GMCDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "GMCDB";
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    3            �            1259    32878 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false    3            �            1259    32877    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    3    216            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    215            �            1259    32887    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false    3            �            1259    32886    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    3    218            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    217            �            1259    32871    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false    3            �            1259    32870    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    214    3            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    213            �            1259    32894 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false    3            �            1259    32903    auth_user_groups    TABLE     ~   CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false    3            �            1259    32902    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    3    222            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    221            �            1259    32893    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    3    220            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    219            �            1259    32910    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false    3            �            1259    32909 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    224    3            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    223            �            1259    32969    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false    3            �            1259    32968    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    226    3            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    225            �            1259    32862    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false    3            �            1259    32861    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    212    3            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    211            �            1259    32853    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false    3            �            1259    32852    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    210    3            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    209            �            1259    32998    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false    3            �            1259    33053    ebilling_category    TABLE     �   CREATE TABLE public.ebilling_category (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    color character varying(50) NOT NULL,
    is_enabled boolean NOT NULL,
    type_id bigint NOT NULL
);
 %   DROP TABLE public.ebilling_category;
       public         heap    postgres    false    3            �            1259    33052    ebilling_category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ebilling_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.ebilling_category_id_seq;
       public          postgres    false    241    3            �           0    0    ebilling_category_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.ebilling_category_id_seq OWNED BY public.ebilling_category.id;
          public          postgres    false    240            �            1259    33009    ebilling_categorytype    TABLE     �   CREATE TABLE public.ebilling_categorytype (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    is_enabled boolean NOT NULL
);
 )   DROP TABLE public.ebilling_categorytype;
       public         heap    postgres    false    3            �            1259    33008    ebilling_categorytype_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ebilling_categorytype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.ebilling_categorytype_id_seq;
       public          postgres    false    229    3            �           0    0    ebilling_categorytype_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.ebilling_categorytype_id_seq OWNED BY public.ebilling_categorytype.id;
          public          postgres    false    228            �            1259    33091    ebilling_client    TABLE     �  CREATE TABLE public.ebilling_client (
    id bigint NOT NULL,
    fullname character varying(100) NOT NULL,
    billing_address character varying(300) NOT NULL,
    city character varying(50),
    district character varying(50) NOT NULL,
    province character varying(50) NOT NULL,
    pincode character varying(6),
    country character varying(50) NOT NULL,
    email character varying(200),
    phone character varying(10),
    mobile character varying(10) NOT NULL,
    pan_no character varying(10),
    vat character varying(10),
    account_type character varying(10) NOT NULL,
    opening_balance integer,
    profile_pic character varying(100) NOT NULL,
    identity_doc character varying(50),
    document_no character varying(50),
    credit_allowed boolean NOT NULL,
    credit_limit integer,
    remark character varying(255),
    company_id bigint NOT NULL,
    is_active boolean NOT NULL
);
 #   DROP TABLE public.ebilling_client;
       public         heap    postgres    false    3            �            1259    33143    ebilling_client_id_seq    SEQUENCE        CREATE SEQUENCE public.ebilling_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.ebilling_client_id_seq;
       public          postgres    false    242    3            �           0    0    ebilling_client_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.ebilling_client_id_seq OWNED BY public.ebilling_client.id;
          public          postgres    false    243            �            1259    33016    ebilling_company    TABLE     �  CREATE TABLE public.ebilling_company (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    email character varying(200),
    phone character varying(10) NOT NULL,
    city character varying(50) NOT NULL,
    district character varying(50) NOT NULL,
    province character varying(50) NOT NULL,
    pincode integer NOT NULL,
    country character varying(50) NOT NULL,
    pan_no character varying(50) NOT NULL,
    reg_no character varying(50),
    reg_date date,
    website character varying(255),
    address character varying(255),
    logo character varying(100) NOT NULL,
    paper_size character varying(10) NOT NULL,
    user_id integer
);
 $   DROP TABLE public.ebilling_company;
       public         heap    postgres    false    3            �            1259    33015    ebilling_company_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ebilling_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.ebilling_company_id_seq;
       public          postgres    false    231    3            �           0    0    ebilling_company_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.ebilling_company_id_seq OWNED BY public.ebilling_company.id;
          public          postgres    false    230            �            1259    33046    ebilling_item    TABLE     h  CREATE TABLE public.ebilling_item (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    decription character varying(255) NOT NULL,
    sale_price integer NOT NULL,
    purchase_price integer NOT NULL,
    picture character varying(100) NOT NULL,
    is_enabled boolean NOT NULL,
    category_id bigint NOT NULL,
    tax_id bigint NOT NULL
);
 !   DROP TABLE public.ebilling_item;
       public         heap    postgres    false    3            �            1259    33045    ebilling_item_id_seq    SEQUENCE     }   CREATE SEQUENCE public.ebilling_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.ebilling_item_id_seq;
       public          postgres    false    3    239            �           0    0    ebilling_item_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.ebilling_item_id_seq OWNED BY public.ebilling_item.id;
          public          postgres    false    238            �            1259    33025    ebilling_itemcategory    TABLE     �   CREATE TABLE public.ebilling_itemcategory (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    is_enabled boolean NOT NULL
);
 )   DROP TABLE public.ebilling_itemcategory;
       public         heap    postgres    false    3            �            1259    33024    ebilling_itemcategory_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ebilling_itemcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.ebilling_itemcategory_id_seq;
       public          postgres    false    3    233            �           0    0    ebilling_itemcategory_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.ebilling_itemcategory_id_seq OWNED BY public.ebilling_itemcategory.id;
          public          postgres    false    232            �            1259    33039    ebilling_tax    TABLE     �   CREATE TABLE public.ebilling_tax (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    rate character varying(5) NOT NULL,
    is_enabled boolean NOT NULL,
    type_id bigint NOT NULL
);
     DROP TABLE public.ebilling_tax;
       public         heap    postgres    false    3            �            1259    33038    ebilling_tax_id_seq    SEQUENCE     |   CREATE SEQUENCE public.ebilling_tax_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.ebilling_tax_id_seq;
       public          postgres    false    3    237            �           0    0    ebilling_tax_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.ebilling_tax_id_seq OWNED BY public.ebilling_tax.id;
          public          postgres    false    236            �            1259    33032    ebilling_taxtype    TABLE     �   CREATE TABLE public.ebilling_taxtype (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    is_enabled boolean NOT NULL
);
 $   DROP TABLE public.ebilling_taxtype;
       public         heap    postgres    false    3            �            1259    33031    ebilling_taxtype_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ebilling_taxtype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.ebilling_taxtype_id_seq;
       public          postgres    false    235    3            �           0    0    ebilling_taxtype_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.ebilling_taxtype_id_seq OWNED BY public.ebilling_taxtype.id;
          public          postgres    false    234            �           2604    32881    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �           2604    32890    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �           2604    32874    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            �           2604    32897    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    32906    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    32913    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            �           2604    32972    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    32865    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211    212            �           2604    32856    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210            �           2604    33056    ebilling_category id    DEFAULT     |   ALTER TABLE ONLY public.ebilling_category ALTER COLUMN id SET DEFAULT nextval('public.ebilling_category_id_seq'::regclass);
 C   ALTER TABLE public.ebilling_category ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    241    240    241            �           2604    33012    ebilling_categorytype id    DEFAULT     �   ALTER TABLE ONLY public.ebilling_categorytype ALTER COLUMN id SET DEFAULT nextval('public.ebilling_categorytype_id_seq'::regclass);
 G   ALTER TABLE public.ebilling_categorytype ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    229    229            �           2604    33144    ebilling_client id    DEFAULT     x   ALTER TABLE ONLY public.ebilling_client ALTER COLUMN id SET DEFAULT nextval('public.ebilling_client_id_seq'::regclass);
 A   ALTER TABLE public.ebilling_client ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    243    242            �           2604    33019    ebilling_company id    DEFAULT     z   ALTER TABLE ONLY public.ebilling_company ALTER COLUMN id SET DEFAULT nextval('public.ebilling_company_id_seq'::regclass);
 B   ALTER TABLE public.ebilling_company ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    230    231    231            �           2604    33049    ebilling_item id    DEFAULT     t   ALTER TABLE ONLY public.ebilling_item ALTER COLUMN id SET DEFAULT nextval('public.ebilling_item_id_seq'::regclass);
 ?   ALTER TABLE public.ebilling_item ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    238    239            �           2604    33028    ebilling_itemcategory id    DEFAULT     �   ALTER TABLE ONLY public.ebilling_itemcategory ALTER COLUMN id SET DEFAULT nextval('public.ebilling_itemcategory_id_seq'::regclass);
 G   ALTER TABLE public.ebilling_itemcategory ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    232    233    233            �           2604    33042    ebilling_tax id    DEFAULT     r   ALTER TABLE ONLY public.ebilling_tax ALTER COLUMN id SET DEFAULT nextval('public.ebilling_tax_id_seq'::regclass);
 >   ALTER TABLE public.ebilling_tax ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    236    237    237            �           2604    33035    ebilling_taxtype id    DEFAULT     z   ALTER TABLE ONLY public.ebilling_taxtype ALTER COLUMN id SET DEFAULT nextval('public.ebilling_taxtype_id_seq'::regclass);
 B   ALTER TABLE public.ebilling_taxtype ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    235    234    235            �          0    32878 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    216   �       �          0    32887    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    218   9�       �          0    32871    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    214   V�       �          0    32894 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    220   ~�       �          0    32903    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    222   ��       �          0    32910    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    224   ��       �          0    32969    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    226   ��       �          0    32862    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    212   e�       �          0    32853    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    210   �       �          0    32998    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    227   s�       �          0    33053    ebilling_category 
   TABLE DATA           Q   COPY public.ebilling_category (id, name, color, is_enabled, type_id) FROM stdin;
    public          postgres    false    241   ��       �          0    33009    ebilling_categorytype 
   TABLE DATA           E   COPY public.ebilling_categorytype (id, name, is_enabled) FROM stdin;
    public          postgres    false    229   ��       �          0    33091    ebilling_client 
   TABLE DATA             COPY public.ebilling_client (id, fullname, billing_address, city, district, province, pincode, country, email, phone, mobile, pan_no, vat, account_type, opening_balance, profile_pic, identity_doc, document_no, credit_allowed, credit_limit, remark, company_id, is_active) FROM stdin;
    public          postgres    false    242   ��       �          0    33016    ebilling_company 
   TABLE DATA           �   COPY public.ebilling_company (id, name, email, phone, city, district, province, pincode, country, pan_no, reg_no, reg_date, website, address, logo, paper_size, user_id) FROM stdin;
    public          postgres    false    231   ��       �          0    33046    ebilling_item 
   TABLE DATA           �   COPY public.ebilling_item (id, name, decription, sale_price, purchase_price, picture, is_enabled, category_id, tax_id) FROM stdin;
    public          postgres    false    239   ^�       �          0    33025    ebilling_itemcategory 
   TABLE DATA           E   COPY public.ebilling_itemcategory (id, name, is_enabled) FROM stdin;
    public          postgres    false    233   {�       �          0    33039    ebilling_tax 
   TABLE DATA           K   COPY public.ebilling_tax (id, name, rate, is_enabled, type_id) FROM stdin;
    public          postgres    false    237   ��       �          0    33032    ebilling_taxtype 
   TABLE DATA           @   COPY public.ebilling_taxtype (id, name, is_enabled) FROM stdin;
    public          postgres    false    235   ��       �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    215            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    217            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);
          public          postgres    false    213            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    221            �           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);
          public          postgres    false    219            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    223            �           0    0    django_admin_log_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 3, true);
          public          postgres    false    225            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);
          public          postgres    false    211            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);
          public          postgres    false    209            �           0    0    ebilling_category_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.ebilling_category_id_seq', 1, false);
          public          postgres    false    240            �           0    0    ebilling_categorytype_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.ebilling_categorytype_id_seq', 1, false);
          public          postgres    false    228            �           0    0    ebilling_client_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.ebilling_client_id_seq', 4, true);
          public          postgres    false    243            �           0    0    ebilling_company_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.ebilling_company_id_seq', 1, true);
          public          postgres    false    230            �           0    0    ebilling_item_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.ebilling_item_id_seq', 1, false);
          public          postgres    false    238            �           0    0    ebilling_itemcategory_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.ebilling_itemcategory_id_seq', 1, false);
          public          postgres    false    232            �           0    0    ebilling_tax_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.ebilling_tax_id_seq', 1, false);
          public          postgres    false    236            �           0    0    ebilling_taxtype_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.ebilling_taxtype_id_seq', 1, false);
          public          postgres    false    234            �           2606    32996    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    216            �           2606    32926 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    218    218            �           2606    32892 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    218            �           2606    32883    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    216            �           2606    32917 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    214    214            �           2606    32876 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    214            �           2606    32908 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    222            �           2606    32941 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    222    222            �           2606    32899    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    220            �           2606    32915 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    224            �           2606    32955 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    224    224            �           2606    32991     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    220            �           2606    32977 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    226            �           2606    32869 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    212    212            �           2606    32867 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    212            �           2606    32860 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    210            �           2606    33004 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    227                       2606    33058 (   ebilling_category ebilling_category_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ebilling_category
    ADD CONSTRAINT ebilling_category_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.ebilling_category DROP CONSTRAINT ebilling_category_pkey;
       public            postgres    false    241            �           2606    33014 0   ebilling_categorytype ebilling_categorytype_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.ebilling_categorytype
    ADD CONSTRAINT ebilling_categorytype_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.ebilling_categorytype DROP CONSTRAINT ebilling_categorytype_pkey;
       public            postgres    false    229                       2606    33135 $   ebilling_client ebilling_client_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.ebilling_client
    ADD CONSTRAINT ebilling_client_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.ebilling_client DROP CONSTRAINT ebilling_client_pkey;
       public            postgres    false    242            �           2606    33023 &   ebilling_company ebilling_company_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.ebilling_company
    ADD CONSTRAINT ebilling_company_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.ebilling_company DROP CONSTRAINT ebilling_company_pkey;
       public            postgres    false    231            �           2606    33051     ebilling_item ebilling_item_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.ebilling_item
    ADD CONSTRAINT ebilling_item_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.ebilling_item DROP CONSTRAINT ebilling_item_pkey;
       public            postgres    false    239            �           2606    33030 0   ebilling_itemcategory ebilling_itemcategory_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.ebilling_itemcategory
    ADD CONSTRAINT ebilling_itemcategory_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.ebilling_itemcategory DROP CONSTRAINT ebilling_itemcategory_pkey;
       public            postgres    false    233            �           2606    33044    ebilling_tax ebilling_tax_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.ebilling_tax
    ADD CONSTRAINT ebilling_tax_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.ebilling_tax DROP CONSTRAINT ebilling_tax_pkey;
       public            postgres    false    237            �           2606    33037 &   ebilling_taxtype ebilling_taxtype_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.ebilling_taxtype
    ADD CONSTRAINT ebilling_taxtype_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.ebilling_taxtype DROP CONSTRAINT ebilling_taxtype_pkey;
       public            postgres    false    235            �           1259    32997    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    216            �           1259    32937 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    218            �           1259    32938 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    218            �           1259    32923 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    214            �           1259    32953 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    222            �           1259    32952 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    222            �           1259    32967 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    224            �           1259    32966 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    224            �           1259    32992     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    220            �           1259    32988 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    226            �           1259    32989 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    226            �           1259    33006 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    227            �           1259    33005 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    227                       1259    33082 "   ebilling_category_type_id_b2ad7485    INDEX     c   CREATE INDEX ebilling_category_type_id_b2ad7485 ON public.ebilling_category USING btree (type_id);
 6   DROP INDEX public.ebilling_category_type_id_b2ad7485;
       public            postgres    false    241                       1259    33104 #   ebilling_client_company_id_86c3c594    INDEX     e   CREATE INDEX ebilling_client_company_id_86c3c594 ON public.ebilling_client USING btree (company_id);
 7   DROP INDEX public.ebilling_client_company_id_86c3c594;
       public            postgres    false    242            �           1259    33089 !   ebilling_company_user_id_d8eb52cb    INDEX     a   CREATE INDEX ebilling_company_user_id_d8eb52cb ON public.ebilling_company USING btree (user_id);
 5   DROP INDEX public.ebilling_company_user_id_d8eb52cb;
       public            postgres    false    231            �           1259    33075 "   ebilling_item_category_id_3b716a48    INDEX     c   CREATE INDEX ebilling_item_category_id_3b716a48 ON public.ebilling_item USING btree (category_id);
 6   DROP INDEX public.ebilling_item_category_id_3b716a48;
       public            postgres    false    239                        1259    33076    ebilling_item_tax_id_1b37bd5b    INDEX     Y   CREATE INDEX ebilling_item_tax_id_1b37bd5b ON public.ebilling_item USING btree (tax_id);
 1   DROP INDEX public.ebilling_item_tax_id_1b37bd5b;
       public            postgres    false    239            �           1259    33064    ebilling_tax_type_id_43945a81    INDEX     Y   CREATE INDEX ebilling_tax_type_id_43945a81 ON public.ebilling_tax USING btree (type_id);
 1   DROP INDEX public.ebilling_tax_type_id_43945a81;
       public            postgres    false    237            	           2606    32932 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    218    214    3276                       2606    32927 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    3281    218    216                       2606    32918 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    214    212    3271                       2606    32947 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    3281    216    222            
           2606    32942 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    3289    220    222                       2606    32961 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    224    214    3276                       2606    32956 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    220    224    3289                       2606    32978 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    212    3271    226                       2606    32983 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    226    220    3289                       2606    33077 P   ebilling_category ebilling_category_type_id_b2ad7485_fk_ebilling_categorytype_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_category
    ADD CONSTRAINT ebilling_category_type_id_b2ad7485_fk_ebilling_categorytype_id FOREIGN KEY (type_id) REFERENCES public.ebilling_categorytype(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.ebilling_category DROP CONSTRAINT ebilling_category_type_id_b2ad7485_fk_ebilling_categorytype_id;
       public          postgres    false    3314    229    241                       2606    33099 J   ebilling_client ebilling_client_company_id_86c3c594_fk_ebilling_company_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_client
    ADD CONSTRAINT ebilling_client_company_id_86c3c594_fk_ebilling_company_id FOREIGN KEY (company_id) REFERENCES public.ebilling_company(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.ebilling_client DROP CONSTRAINT ebilling_client_company_id_86c3c594_fk_ebilling_company_id;
       public          postgres    false    242    231    3316                       2606    33084 B   ebilling_company ebilling_company_user_id_d8eb52cb_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_company
    ADD CONSTRAINT ebilling_company_user_id_d8eb52cb_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.ebilling_company DROP CONSTRAINT ebilling_company_user_id_d8eb52cb_fk_auth_user_id;
       public          postgres    false    220    3289    231                       2606    33065 L   ebilling_item ebilling_item_category_id_3b716a48_fk_ebilling_itemcategory_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_item
    ADD CONSTRAINT ebilling_item_category_id_3b716a48_fk_ebilling_itemcategory_id FOREIGN KEY (category_id) REFERENCES public.ebilling_itemcategory(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.ebilling_item DROP CONSTRAINT ebilling_item_category_id_3b716a48_fk_ebilling_itemcategory_id;
       public          postgres    false    233    3319    239                       2606    33070 >   ebilling_item ebilling_item_tax_id_1b37bd5b_fk_ebilling_tax_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_item
    ADD CONSTRAINT ebilling_item_tax_id_1b37bd5b_fk_ebilling_tax_id FOREIGN KEY (tax_id) REFERENCES public.ebilling_tax(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.ebilling_item DROP CONSTRAINT ebilling_item_tax_id_1b37bd5b_fk_ebilling_tax_id;
       public          postgres    false    237    239    3323                       2606    33059 A   ebilling_tax ebilling_tax_type_id_43945a81_fk_ebilling_taxtype_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.ebilling_tax
    ADD CONSTRAINT ebilling_tax_type_id_43945a81_fk_ebilling_taxtype_id FOREIGN KEY (type_id) REFERENCES public.ebilling_taxtype(id) DEFERRABLE INITIALLY DEFERRED;
 k   ALTER TABLE ONLY public.ebilling_tax DROP CONSTRAINT ebilling_tax_type_id_43945a81_fk_ebilling_taxtype_id;
       public          postgres    false    3321    237    235            �      x������ � �      �      x������ � �      �     x�m�Q�� @��)z�U	���{��FQ���ڤJә�����_��cG��ô.��m����.o�U8�3�C��o��^P)TA�����*���E�k����
�b���}|>�yR�� �\N�d���,	2�X���;��2�ʠ >��s��'/B4w���U���M1x=��,
�GЖק,�O���	��	�kmJc�<���yZ�Wۭ�W(#��\��IH�'������n_5u���ӧ�ڣ0���^�,�����^�جW�
�X�az��O���}�)�#� ����0�Y�>R��<��:/���c��ӈ!o�(n��ood[q��@�'qA���:	q0�7�@5�`�o�l4��[ŀ	;0uc��'�A�ID�pN�bU8Ej;�ARˠe��1T+��fJ�,�k�b���5�G�W�V���\l��q���8���1X�g�lxR�W�Fl����¶cs�%~o��)����pL3Op�����I��/�ؤ����S:���	���)'J�x����0i��� �4��p      �     x�m�]O�0���Wx�a��[�-1q6� 
�����n��2a_��I��su���=���]��Z).kQ�fZ��>��m/Q�~����q�(-q��C<����ͮ;��XFǹ؏4O�ⶼa�� t������u �r���6v�Q���I���e&���6�K-V��Vj�?�W%�6g'���"���.� �L
G���|�v�Ƥ�z0���QAU�g^F�r�+5k����	�c�y�����1�)����5R��FoֿV���&��;[_l˲>�oa8      �      x������ � �      �      x������ � �      �   t   x�}α
�@��z�)�����]g��N�H
A��?����c��@�m�MŹ�-&1	`��^�I��|�U?���g���KJ$FpX�Gl��y_w�vA����Ť��;�[��#��K^,5      �   �   x�e�K
�0DךÔ:Iw��m�+�[���	%	�i��!�� �|r�4tdG}S��VI�B\Icư��r���)�i�\�g�<��7�B��%�������.�6۷s\����3f�`�5�rX�~��6'�Lo�~ ���\i      �   _  x����r�0���S��F�:�,��(�8��Ti��.�MB��p�?��]�P�C?�~�/��
B���۶@��D�a?���V�����?	�(9aa���QJN8P��ha����S���b��v8ǂ���o��*c��Ca	�oz�Ĩ���޼��l����Q�!N�V���'y�j�>����m�iJh�h2�Dc��3���iZ[���u�9�ꐦbw�FS�F7�2Ň�o��TDl �A��>�E�|�J���6
������N��	���Ǔ�)HH��A"�����m_�`V���h�i�ܦWn���7v�t	�L�ɞ�3�3��8�LT�����%�J�4�2L��-gu��D���aX��$W�7)2	�2F]Όax��둫��Z�4T���~{/>|s LBƩbr��.,�j��х{�m���WI$�k�D���.xw���3����{v��ꊲRI�U���c�Y���"�RrMc>�qg�n}<��X��XQ^�w����tL�_��fG��ʱ�B��!�Ğ0���á�d��2�#�*b+H�������A��t����{d\������=*��!R���_��t����      �   .  x���ˮ�@  �u����<`�a��E��ib Ay����I����O8�~�dH�a��?���ȋ|��k*���"��ɪ��D�jx�7�t=2�m.F󋽋�� ��e���_�$�(9Kh�Ǎ��2j�h��&	�P��B�b��he�f����Il0�%�3M������A�{=�tE�V��ă��S=q�W;���竪����H�w$��`�U�.
�V^������C�,�?y{}؎��Ѕ����C �9��|T���R�D��;���)�e6�R�j���vbc��i�I�wEr�*��j��Z�#�{�de�jWX)MV�XT���$
2B" ~5���R���js�}@���e��t�ӤiV+�ޖ��+-���ͳ^�\)�m�j�{����k��y�4�)�y3�h�[�J�*�RU�gH{_���N�Z6�e��^3SQ;��v�/�l{^m����{)ѼM(ʚ�j����L�Z�����);�\f�K���U���}I%6H�6OE"�ځ��k���^HJ�k��b6���      �      x������ � �      �      x������ � �      �   �  x����n�0���S�Ͽ�}��v-��(R�a�Aۊ�L�Yހ=}�&Mt�q:�@~��Kb7�W�hEUO�d�Gd���m���1���A��vC����ahKR���.d�C	f���i��S����$����d���p���T�V�0V���? ��W�?Qzs�JW��>��EG�'���>�Je�;��!��m�n�.Q����|���pWl��^��������#�{;\<?��@�V3~؄^��:�N!��z,�	x�;��Y��ۇ"Ճ�y��C>����8PM����d�W���D���`�?�|��65�%�'˹�4�A��,�h�k���P/��j2 _L#��jv�����I�G��7qz\�򟂕@��\I��W�GT,ES�w�~��b�xE2��      �   �   x�E�A�0DןSp �m)Fv�	Q�&���������n4��L&yO�=�Π�ouڼBZ��oq�nt��a0H#k��r/�*�"�p�H5��eB����Z̓,A.KΡ�'A�2W�$�<�"����@F6jQ�4aЙڤWb5�3��]��K[�CT���#��-�β�pT �;K����G�      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     