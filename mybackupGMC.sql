PGDMP                         z            GMCNEPAL_DB    14.4    14.4     j           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            k           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            l           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            m           1262    16551    GMCNEPAL_DB    DATABASE     q   CREATE DATABASE "GMCNEPAL_DB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "GMCNEPAL_DB";
                postgres    false            \          0    16578 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    216   <       ^          0    16587    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    218   Y       Z          0    16571    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    214   v       `          0    16594 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    220   �       b          0    16603    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    222   d       d          0    16610    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    224   �       f          0    16669    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    226   �       X          0    16562    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    212   �       V          0    16553    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    210   "       g          0    16698    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    227   �       w           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    215            x           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    217            y           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 24, true);
          public          postgres    false    213            z           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    221            {           0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);
          public          postgres    false    219            |           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    223            }           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          postgres    false    225            ~           0    0    django_content_type_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_content_type_id_seq', 6, true);
          public          postgres    false    211                       0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);
          public          postgres    false    209            \      x������ � �      ^      x������ � �      Z     x�]�K��0��ur
N0j£�z�Q�B�b�:�h�����I�%��o��i�g�f��c�Y����G�<��ЂRq�0G��f�a����[�m��Le���4u}0�x`+� �	{�}�R��NT����v�����֝d�~O]D�l�	�����<,�����ӺB�[ZA)���T���qu�<�͏>��_��� ��m�.2�)H���:x�ޟ8�1WY��'���`:Y��;�LL�vf���x댰j'�k�2�      `   �   x�U��n�@����.�5��Cg�LbRӐ���H4&f,ҡ��R%}��p�����|,���(��!ܲ)1=�	�K��󣩢�ۅ�r!��M�u�a�|��C��yn~��:QD�vG�����H	����|!@(��^�g'	�Wcl0?e�kݜ��׍��W����l��:��|�(.	�{�޵,��a9      b      x������ � �      d      x������ � �      f      x������ � �      X   W   x�M�K
�0�y����M�P�C�.z{E��LOn�!љ='���\��
K�!'�o�k��JU̴�d�f���)?�~��pM^%�      V   �  x����n� ��{_���g�4B	u��qG��/��D�������̟�qw�s2sJ���!���6Y�:�yC��?H;ڳ�!�"~��@:���gE��\R�K��y���*I�d��ݫ8?������@�>����P��w�ޙ\
�������N�ޞr����?�#��� �'0���j��T�8e���v�XL�l�[c��g�1����rR��i�hk�3i�A
1�p�T��#�]nM�%�G��MV�è1��q:��$lqu����THT7H䰿VZڷc�-�_�I]|�^Y�hg�:�o+aB�&���������nR�M��(g���~���ƨjg�y�0*����&	�X�K4	ú�,�_�u/��H&����-;&��}���|�K<Tn�)�~�c�=�����{8�Ktd�      g     x���n�0  �g���/�b)�d0F7d��,!Z/�r
_�sĠ9Rk< ��!N��:O��|FS�������v�x�v��oS��A$�ّ��rIw���M[q(�znr�S/���~m��xڎ(Kt����.�����H~%�PR����VFo��T�#rYI"�)��Ǉ�דѻ	�x�9��Q�%����0hl�{z��
$���<�YD3�=���g�󧎸L!�Z�Rmff�È����K����L!�F a�
���R���`P     