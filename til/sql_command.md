# sql コマンド学習メモ

```
■SELECT
select [distinct] *|列名i [[as] 列別名i] from 表名

　・列名iには計算式を書ける
　・nullを含む計算の解はnul
　・order byでのみ列別名を使用可

■WHERE
where 列名 比較演算子 条件値
where 列名 [not] between 下限値 and 上限値
where 列名 [not] in(値i)
where 列名 [not] like 条件値 [escape エスケープ記号]
	% 任意の文字列
	_ 任意の一文字
where 列名 is [not] null

where 条件1 [and|or] 条件2 [and|or] … 条件n
	優先順位は () > not > and > or の順
	( )で囲めば明示的に最高(?)順位にできる

where 条件式 order by 基準列i [ASC|DESC]
	col1 asc, col2 descといった複数指定も可

■関数/Functions
getdate()
	現在日付を取得
coalesce(列名,代替値);
	列名内のnull値を代替値に置き換える
	ex) nullを数字の0として扱いたい場合に重宝?
sum(列名)
	列値の合計値(null値を除く)
avg(列名)
	列値の平均値(null値を除く)
max(列名)
	列値の最大値(null値を除く)
min(列名)
	列値の最小値(null値を除く)
count(列名)
	列値の行数(null値を除く)
count(*)
	表の行数
count(distinct 列名)
	列値の種類数(null値を除く)

※集合関数にgroup byは必須ではない

■グルーピング
group by 列名 [having 集合関数を用いた条件]
	列名をグループ化し、
	条件にヒットしたもののみ表示

	・グループ化した場合、SELECTで指定できる属性は
	　group byで指定した属性のみ
	　（ただし集合関数であれば可能）

select bno,AVG(salary) from SHAIN group by BNO;
	部門ごとの平均基本給を検索.

■内部結合
select *|表名i.列名i
from 表名1 [[as] 表別名1] [inner] join 表名2 [[as] 表別名2]
on 表名1.結合キー = 表名2.結合キー
	表1と表2を、結合キーで結合した表を返す

	・join ～ on ～は複数指定可
	・結合キー列が等しいデータのみ結合する
	・表別名iを指定したら、
	　表名iの部分を表別名iで記述しなければならない
	・表別名iのスコープは文の内（文頭から文末まで）

■外部結合
select *|表名i.列名i
from 表名1 [[as] 表別名1]
left|right|full [outer] join 表名2 [[as] 表別名2]
on 表名1.結合キー = 表名2.結合キー
	基本的な書式は内部結合と同じだが…

	left： (join句の)左側に記述された表のみに存在する行も返す
	right: (join句の)右側に記述された表のみに存在する行も返す
	full:  left + right の働き

■副問い合わせ
select sname from SHAIN
where SALARY >= (select avg(salary) from shain);
	shain表から平均給与以上の給与をもらってる社員名を返す
		・where句に集合関数はかけない salary>=avg() は無理.

■テーブルの行数カウント
select count(*) from tablename

-------------------------------------------
▽DML = Data Manipulation Language データ操作言語
-------------------------------------------

■select
select文もDMLらしいです．

■insert
insert into 表名[(列名i)] values(挿入値i)
	表名（の列名i）に、新しく挿入値iを持つ行を追加
	
insert into 表名[(列名i)] select …
	表名（の列名i）に、select…から取得した行を追加	

	・列名iにて指定されていない列にはnullが入る
	・挿入値iに明示的にnullを入れることも可
	・挿入元と挿入先とでは列数・順番・型をそろえること

■update
update 表名 set 列名i=更新後の値i [where 条件式]
	表名の 条件式に合致する行の 列名iを更新後の値iに変更

	・where句を略すと全件が更新対象に
	・更新後の値iには、計算式や単一行サブクエリを指定可

■delete
delete from 表名 [where 条件式]
	表明から条件式にマッチする行を削除

	・where句を略すると表全行が削除対象に
	・行データは削除するが、表自体は削除されない
	（・主に主キーを指定して一行削除を行う）

-------------------------------------------
▽DCL = Data Control Language データ制御言語
-------------------------------------------

■begin tran
begin tran
	トランザクションを開始する。
	前のトランザクションは消される。

■commit
commit;
	トランザクションを確定（ログファイルへの反映）する。
	確定後，トランザクションは消える．

	・トランザクションが開始されていない場合、
	　一文ごとに暗黙的にcommitが実行される。
	・DDL文の前後には自動的にcommitが入る．
	　→DDL文に入る前に明示的にトランザクションを終了するがマナー．

■rollback
rollback;
	トランザクションをロールバック終了する．
	確定後，トランザクションは消える．

-------------------------------------------
▽DDL = Data Defination Language データ定義言語
-------------------------------------------

■create table
create table 表名(
列名1 データ型1 列制約1.1, 列制約1.2 …,
列名2 データ型2 列制約2.1, 列制約2.2 …,
…
列名n データ型n 列制約n.1, 列制約n.2,
表制約1(対象列1.1,対象列1.2…),
表制約2(対象列2.1,対象列2.2…),
…
表制約n(対象列n.1,対象列n.2…),
);
	表名を新規する

	・データ型
	データ型名(データサイズ)
		numeric(5), char(10), date など
		numericのサイズ指定を略すと，18になる

	・制約
	primary key
		主キー制約．
		重複およびnull値を許さない．
	not null
		not null制約．
		null値を許さない．
	unique
		一意制約．
		重複を許さないが，null値は例外．
		（SQL Serverの場合はnull値の重複も認めない）
	references 親表(主キー)
		参照整合性制約，列制約構文．
		参照先の表の主キーを書く感じ．
	foreign key (子表の外部キー列) references 親表(主キー)
		参照整合性制約，表制約構文．
		自分の外部キーと，その参照先を書く感じ．
	check(条件式)
		check制約．
		条件式が真であれば，挿入・更新が可能となる．

■Drop
drop table 表名
	表名を削除する．
	表内の行も含めて，表自体が削除される．

■Alter
alter table 表名 add [column] 列名 データ型
	表名に新しい要素を追加する．

alter table 表名 drop [column] 列名
	表名から要素 列名 を削除する．

	※RDBMSによって column が必要だったり不要だったり…

begin tran
	insert
	insert
	begin tran
		delete
		delete
		begin tran
			update
		commit;
	rollback;
commit;
```
