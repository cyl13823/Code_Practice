#include <stdio.h>
#include </opt/homebrew/Cellar/gsl/2.7.1/include/gsl/gsl_types.h>
#include </opt/homebrew/Cellar/gsl/2.7.1/include/gsl/gsl_errno.h>
#include </opt/homebrew/Cellar/gsl/2.7.1/include/gsl/gsl_db.h>

int main(void) {
    gsl_db *db;
    gsl_rng *r;
    int i;

    /* 開啟或創建資料庫 */
    db = gsl_db_open("example.db", "w");

    /* 添加一個名為 "data" 的資料表 */
    gsl_db_add_table(db, "data", 3, "ID", "Name", "Value");

    /* 使用 GSL 提供的亂數產生器創建一些假數據 */
    r = gsl_rng_alloc(gsl_rng_mt19937);
    
    for (i = 0; i < 10; i++) {
        char id[16];
        snprintf(id, sizeof(id), "ID%d", i);
        gsl_db_insert_row(db, "data", id, "Name", gsl_rng_uniform(r));
    }

    gsl_rng_free(r);

    /* 查詢並輸出資料表內容 */
    gsl_db_query(db, "SELECT * FROM data");

    /* 關閉資料庫 */
    gsl_db_close(db);

    return 0;
}