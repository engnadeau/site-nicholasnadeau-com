import { getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    { text: 'Home', href: '/' },
    { text: 'About', href: '#about' },
    { text: 'Blog', href: '#blog' },
  ],
};

export const footerData = {
  links: [],
  secondaryLinks: [
    { text: 'Home', href: '/' },
    { text: 'About', href: '#about' },
    { text: 'Blog', href: '#blog' },
  ],
  socialLinks: [
    { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
    { ariaLabel: 'Github', icon: 'tabler:brand-github', href: 'https://github.com/engnadeau', target: '_blank' },
  ],
};
