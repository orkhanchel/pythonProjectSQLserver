CREATE
TABLE[Parent]
(
    ID INT PRIMARY KEY,
ParentID INT,
Name NVARCHAR(255),
FOREIGN
KEY(ParentID)
REFERENCES
Parent(ID)
)


INSERT
INTO
Parent(ID, ParentID, Name)
VALUES
(1, NULL, N'Notariat fəaliyyəti'),
(2, NULL, N'Vətəndaşlıq vəziyyəti aktlarının dövlət qeydiyyatı'),
(3, NULL, N'Məhkumluq barədə arayışların verilməsi'),
(4, NULL, N'Sürücülük vəsiqələrinin dəyişdirilməsi'),
(5, NULL, N'Şəxsiyyət vəsiqələrinin verilməsi və dəyişdirilməsi'),
(6, NULL, N'Ümumvətəndaş pasportlarının verilməsi və dəyişdirilməsi'),
(7, NULL, N
 'Arxiv arayışlarının, arxiv sənədlərindən çıxarışların, arxiv sənədlərinin təsdiq olunmuş surətlərinin verilməsi'),

(8, 1, N'Əqdlərin və etibarnamələrin təsdiq edilməsi'),
(9, 1, N'Vərəsəlik hüququ haqqında şəhadətnamələrin verilməsi'),
(10, 1, N'Dəniz protestlərinin tərtib edilməsi'),
(11, 1, N'Ər-arvadın ümumi əmlakındakı paya mülkiyyət hüququ haqqında şəhadətnamənin verilməsi'),
(12, 1, N'Fiziki və hüquqi şəxslərinn ərizələrinin başqa fiziki və hüquqi şəxslərə verilməsi'),
(13, 1, N'İcra qeydlərinin aparılması'),
(14, 1, N'Notariusun verdiyi və ya təsdiq etdiyi sənəd itirildikdə onun dublikatının verilməsi'),
(15, 1, N'Sənədlərdəki imzaların həqiqiliyinin təsdiq edilməsi'),
(16, 1, N'Sənədlərin bir dildən başqa dilə tərcüməsinin düzgünlüyünün təsdiq edilməsi'),
(17, 1, N'Sənədlərin surətlərinin və sənədlərdən çıxarışların düzgünlüyünün təsdiq edilməsi'),
(18, 1, N'Sənədlərin təqdim olunduğu vaxtın təsdiq edilməsi'),
(19, 1, N'Şəxsin müəyyən yerdə olması faktının təsdiq edilməsi'),
(20, 1, N'Şəxsin sağ olması faktının təsdiq edilməsi'),
(21, 1, N'Şəxslə foto şəkildəki şəxsin eyniliyinin təsdiq edilməsi'),
(22, 1, N'Sübutların təmin edilməsi'),
(23, 1, N'Veksellərə protestlərin tərtib edilməsi'),
(24, 1, N'Xaricdə istifadə üçün nəzərdə tutulan sənədlərə dair apostil verilməsi üçün sənədlərin qəbulu'),
(25, 2, N'Adın, ata adının və soyadın dəyişdirilməsinin qeydə alınması'),
(26, 2, N'Şəxsiyyət vəsiqəsində ailə vəziyyəti barədə məlumatın dəyişdirilməsi'),
(27, 2, N
 'Vətəndaşlıq vəziyyəti aktlarının qeydindəki səhvlərin düzəldilməsi və onlarda dəyişiklik edilməsi, vətəndaşlıq vəziyyəti aktları qeydlərinin ləğvi, vətəndaşlıq vəziyyəti aktlarının itmiş qeydlərinin bərpası'),
(28, 2, N'Ailə üzvləri haqqında arayış'),
(29, 2, N'Atalığın müəyyən edilməsinin qeydə alınması'),
(30, 2, N'Doğumun qeydə alınması'),
(31, 2, N'Nikahın pozulmasının qeydə alınması'),
(32, 2, N'Nikahın qeydə alınması'),
(33, 2, N'Ölümün qeydə alınması'),
(34, 2, N'Övladlığa götürmənin qeydə alınması'),
(35, 2, N
 'Vətəndaşlıq vəziyyəti aktlarının dövlət qeydiyyatı haqqında şəhadətnamələrin (təkrar şəhadətnamələrin) verilməsi'),
(36, 2, N'Ailə vəziyyəti haqqında arayış'),
(37, 3, N'Zəruri olan sənədlərin siyahısı'),
(38, 3, N'İştirak etməli olan şəxslərin siyahısı'),
(39, 3, N'Müddət'),

(40, 8, N'Etibarnamələrin təsdiqi'),
(41, 8, N'Daşınmaz əmlakın renta müqaviləsinin təsdiqi'),
(42, 8, N'Daşınmaz əmlakın alqı-satqı müqaviləsinin təsdiqi'),
(43, 8, N'Daşınmaz əmlakın bağışlanması müqaviləsinin təsdiqi'),
(44, 8, N'Daşınmaz əmlakın dəyişdirilməsi müqaviləsinin təsdiqi'),
(45, 8, N'İcarə müqaviləsinin təsdiqi'),
(46, 8, N'İpoteka müqaviləsinin təsdiqi'),
(47, 8, N'Miras paya sərəncam verilməsinə dair müqavilənin təsdiqi'),
(48, 8, N'Mirasın bölüşdürülməsinə dair sazişin bağlanması'),
(49, 8, N'Nəqliyyat vasitəsinin özgəninkiləşdirilməsinə dair müqavilənin təsdiqi'),
(50, 8, N'Qarışıq müqavilənin təsdiqi'),
(51, 8, N'Sonrakı ipoteka müqaviləsinin təsdiqi'),
(52, 8, N'Yaşayış sahəsinin kirayə verilməsi müqaviləsinin təsdiq edilməsi'),
(53, 9, N'Qanun üzrə vərəsəlik şəhadətnaməsinin verilməsi'),
(54, 9, N'Vəsiyyətnamə üzrə vərəsəlik şəhadətnaməsinin verilməsi'),

(55, 40, N'Nəqliyyat vasitəsindən istifadə edilməsinə dair etibarnamənin təsdiqi'),
(56, 40, N'Nəqliyyat vasitəsinə sərəncam verilməsinə dair etibarnamənin təsdiqi'),
(57, 40, N'Sair etibarnamələrin təsdiqi'),
(58, 41, N'Daşınmaz əmlakın haqq müqabilində verilməsi barədə renta müqaviləsinin təsdiqi'),
(59, 41, N'Daşınmaz əmlakın pulsuz verilməsi barədə renta müqaviləsinin təsdiqi'),
(60, 42, N'Zəruri olan sənədlərin siyahısı'),
(61, 42, N'İştirak etməli olan şəxslərin siyahısı'),
(62, 42, N'Dövlət rüsumunun məbləği'),
(63, 43, N'Zəruri olan sənədlərin siyahısı'),
(64, 43, N'İştirak etməli olan şəxslərin siyahısı'),
(65, 43, N'Dövlət rüsumunun məbləği'),
(66, 44, N'Zəruri olan sənədlərin siyahısı'),
(67, 44, N'İştirak etməli olan şəxslərin siyahısı'),
(68, 44, N'Dövlət rüsumunun məbləği'),
(69, 45, N'Zəruri olan sənədlərin siyahısı'),
(70, 45, N'İştirak etməli olan şəxslərin siyahısı'),
(71, 45, N'Dövlət rüsumunun məbləği'),
(72, 46, N'Zəruri olan sənədlərin siyahısı'),
(73, 46, N'İştirak etməli olan şəxslərin siyahısı'),
(74, 46, N'Dövlət rüsumunun məbləği'),

(75, 55, N'Zəruri olan sənədlərin siyahısı'),
(76, 55, N'İştirak etməli olan şəxslərin siyahısı'),
(77, 55, N'Dövlət rüsumunun məbləği'),
(78, 56, N'Zəruri olan sənədlərin siyahısı'),
(79, 56, N'İştirak etməli olan şəxslərin siyahısı'),
(80, 56, N'Dövlət rüsumunun məbləği'),
(81, 57, N'Zəruri olan sənədlərin siyahısı'),
(82, 57, N'İştirak etməli olan şəxslərin siyahısı'),
(83, 57, N'Dövlət rüsumunun məbləği'),
(84, 58, N'Zəruri olan sənədlərin siyahısı'),
(85, 58, N'İştirak etməli olan şəxslərin siyahısı'),
(86, 58, N'Dövlət rüsumunun məbləği'),
(87, 59, N'Zəruri olan sənədlərin siyahısı'),
(88, 59, N'İştirak etməli olan şəxslərin siyahısı'),
(89, 59, N'Dövlət rüsumunun məbləği')

SELECT * FROM
Parent

SELECT
p.ID,
COALESCE(p.Name, '')
AS
Name_Parent,
COALESCE(c.Name, '')
AS
Name_Child1,
COALESCE(b.Name, '')
AS
Name_Child2,
COALESCE(d.Name, '')
AS
Name_Child3,
COALESCE(t.Name, '')
AS
Name_Child4
FROM
Parent
p
LEFT
JOIN
Parent
c
ON
p.ID = c.ParentID
LEFT
JOIN
Parent
b
ON
c.ID = b.ParentID
LEFT
JOIN
Parent
d
ON
b.ID = d.ParentID
LEFT
JOIN
Parent
t
ON
d.ID = t.ParentID
WHERE
p.ParentID
IS
NULL

SELECT * INTO
Parent_Copy
FROM
Parent
SELECT * FROM
Parent_Copy

CREATE
TRIGGER
trg_Parent_Copy
ON
Parent
AFTER
INSERT, UPDATE, DELETE
AS
BEGIN
SET
NOCOUNT
ON;

IF(EXISTS(SELECT * FROM
inserted) AND
EXISTS(SELECT * FROM
deleted))
BEGIN
UPDATE
at
SET
ID = i.ID,
ParentID = i.ParentID,
Name = i.Name
FROM
Parent_Copy
at
INNER
JOIN
inserted
i
ON
at.ID = i.ID
INNER
JOIN
deleted
d
ON
at.ID = d.ID;
END

IF(EXISTS(SELECT * FROM
inserted) AND
NOT
EXISTS(SELECT * FROM
deleted))
BEGIN
INSERT
INTO
Parent_Copy(ID, ParentID, Name)
SELECT
ID, ParentID, Name
FROM
inserted;
END

IF(EXISTS(SELECT * FROM
deleted) AND
NOT
EXISTS(SELECT * FROM
inserted))
BEGIN
DELETE
at
FROM
Parent_Copy
at
INNER
JOIN
deleted
d
ON
at.ID = d.ID;
END
END

CREATE
TABLE
testorxan
(
    ID INT,
Name NVARCHAR(10)
);

CREATE
OR
ALTER
PROCEDURE
copy_test_table
AS
BEGIN
DECLARE @ v_count
INT;

SELECT @ v_count = COUNT(*)
FROM
INFORMATION_SCHEMA.TABLES
WHERE
TABLE_NAME = 'testorxan';

IF @ v_count = 1
BEGIN
EXEC
sp_executesql
N
'DROP TABLE testorxan';
END
EXEC
sp_executesql
N
'CREATE TABLE testorxan (ID INT, Name NVARCHAR(10))';

PRINT
'New table created:';
END;

EXEC
copy_test_table;
SELECT * FROM
testorxan;
EXEC
sp_columns
'testorxan';

/ *CREATE
PROCEDURE
SALAM
AS
BEGIN
SELECT
N
'HELLO VSEM'
AS
PRIVET
END

EXEC
SALAM

CREATE
PROCEDURE
DATE
AS
BEGIN
SELECT
GETDATE()
AS
DAY
END

EXEC
DAY * /

CREATE
OR
ALTER
FUNCTION
dbo.fn_get_servicename
(
    @ service_id int
)
RETURNS
nvarchar(255)
AS
BEGIN
DECLARE @ ServiceName
nvarchar(255)

SELECT @ ServiceName = ServiceName
FROM[Services]
WHERE
ID =


@service_id


RETURN @ ServiceName
END
GO

SELECT
ID,
dbo.fn_get_servicename(ID, 1),
dbo.fn_get_servicename(ID, 2),
dbo.fn_get_servicename(ID, 3)
FROM[Services]
GO

WITH
DirectReports(ID, ParentID, ServiceName, EmployeeLevel)
AS
(
    SELECT
    ID,
    ParentID,
    ServiceName,
    0 AS EmployeeLevel FROM dbo.Services
    WHERE ParentID IS NULL
    UNION ALL
    SELECT
    e.ID,
    e.ParentID,
    e.ServiceName,
    EmployeeLevel + 1
    FROM dbo.Services AS e INNER JOIN DirectReports AS d ON e.ParentID = d.ID
)
SELECT
ID, ParentID, dbo.fn_get_servicename(ParentID)
AS
ParentServiceName, ServiceName, EmployeeLevel
FROM
DirectReports
ORDER
BY
EmployeeLevel
GO
