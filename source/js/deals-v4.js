(() => {
  const input = document.getElementById('deal-search-input');
  if (!input) return;
  const results = document.getElementById('deal-search-results');
  const status = document.getElementById('deal-search-status');
  const en = document.documentElement.lang === 'en';
  let index;
  const search = async () => {
    try {
      if (!index) index = fetch(input.dataset.index).then(r => {
        if (!r.ok) throw new Error('Search unavailable');
        return r.json();
      });
      const rows = await index;
      const query = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
      const hits = query.length ? rows.filter(row => query.every(q => (row.title + ' ' + row.description).toLocaleLowerCase().includes(q))).slice(0, 20) : [];
      results.replaceChildren(...hits.map(row => {
        const li = document.createElement('li');
        const link = document.createElement('a');
        link.href = row.url;
        link.textContent = row.title;
        li.append(link);
        return li;
      }));
      status.textContent = query.length ? (en ? `${hits.length} results (up to 20)` : `${hits.length} 条结果（最多20条）`) : '';
    } catch {
      index = null;
      status.textContent = en ? 'Search unavailable. Focus again to retry.' : '搜索暂不可用，请重新聚焦重试。';
    }
  };
  input.addEventListener('focus', search);
  input.addEventListener('input', search);
})();
