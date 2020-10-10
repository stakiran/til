# Vuex

## vuex
- ストアというグローバルシングルトン的なデータ構造をつくる
- データの更新は commit にて行う
    - `this.$store.commit('mutation_type, payload)`
- なぜ？
    - 呼び出し方を統一できるから
        - commit 側で実行ログが取れる
    - View側は「使いたい更新操作だけ使う」で済むから
        - 例: 使える mutation_type を定数で一覧にして「こいつらだけ使え」という運用にする
        - mutation の中で何してるかは感知しなくていい
    - 同期と非同期を分けて実装できるから
        - 同期は mutations
        - 非同期は actions に定義し、mutation を呼び出す
        - ↑ このモデルで統一している

## マッピングした getter や mutation に引数を渡す
- マッピング時は function のみマッピングする
- 引数はマッピング先で上手いことつくってから渡す
    - store 側の引数定義に従う
    - vuex ドキュメントに従えば payload になってるはず

マッピング時

```javascript
    ...mapGetters("Monster",["hp","name"]),

    ...mapMutations({
      initialize: "Monster/init",
      attack: "Monster/decrease_hp"
    }),

```

使うとき

```
    <button v-on:click="initialize(status_of_monster)">create monster</button>
    <button v-on:click="attack(my_attack_damage)">attack the monster</button>

===

  data: function() {
    return {
      using_hp: 45,
      using_name: 'Slime'
    }
  },
  computed: {
    ...mapGetters("Monster",["hp","name"]),
    status_of_monster: function(){
      // ★store側で payload.hp と payload.name を使ってるので同じ構造を使う
      return {
        hp: this.using_hp,
        name: this.using_name
      }
    },
    my_attack_damege: function(){
      return {
        damage: this.get_random_number_0_to_x(20) // methods で定義してる乱数出力関数
      }
    },
  },

```
