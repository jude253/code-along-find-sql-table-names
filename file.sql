// comment
-- comment
# comment

select *
from (
  select col1 from test.test_a join test.test_a1 on a.col1 = a1.col1) a
left join test.test_b b # comment
on a.col1 = b.col2
left join
    test.test_c c // comment
/* sdfiujsdf
iuhsidfgoisdf
 lkjsdfgoijsdf */
on b.col2  = c.col3 //
left join
   (select
       col4
    from
    /* sdfiujsdf
iuhsidfgoisdf
 lkjsdfgoijsdf */ test.test_d) d

/* sdfiujsdf
iuhsidfgoisdf
 lkjsdfgoijsdf */
on c.col3  = d.col4