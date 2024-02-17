-- 코드를 입력하세요
SELECT 
    UGB.board_id, 
    UGB.writer_id, 
    UGB.title, 
    UGB.price, 
    CASE 
       WHEN UGB.status = 'SALE' THEN '판매중'
       WHEN UGB.status = 'RESERVED' THEN '예약중'
       WHEN UGB.status = 'DONE' THEN '거래완료'
    END
FROM USED_GOODS_BOARD UGB 
WHERE UGB.created_date >= '2022-10-05 00:00:00' and UGB.created_date < '2022-10-06 00:00:00' order by UGB.board_id DESC;