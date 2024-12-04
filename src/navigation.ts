import { getAsset } from './utils/permalinks';

export const headerData = {
  links: [
    { text: 'Home', href: '/' },
    { text: 'Posts', href: '/#posts' },
    { text: 'About', href: '/#about' },
  ],
};

export const footerData = {
  links: [],
  secondaryLinks: [
    { text: 'Home', href: '/' },
    { text: 'Posts', href: '/#posts' },
    { text: 'About', href: '/#about' },
  ],
  socialLinks: [
    { ariaLabel: 'RSS', icon: 'tabler:rss', href: getAsset('/rss.xml') },
    { ariaLabel: 'Github', icon: 'tabler:brand-github', href: 'https://github.com/engnadeau', target: '_blank' },
  ],
  footNote: `© ${new Date().getFullYear()} Nicholas Nadeau. All rights reserved.`,
};
